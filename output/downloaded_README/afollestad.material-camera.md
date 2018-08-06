# Material Camera (Deprecated)

No longer maintaimed. 

Android's video recording APIs are very difficult to figure out, especially since a lot of manufacturers
like to mount their camera sensors upside down or sideways. This library is a result of lots of research
and experimentation to get video recording to work universally.

<img src="https://raw.githubusercontent.com/afollestad/material-camera/master/art/showcase1.png" width="800px" />

---

# Notice

Please report any issues you have, and include device information. Camera behavior can be unpredictable
across different Android manufacturers and versions, especially on pre-Lollipop devices. I've done quite
a bit of testing, but it's possible I missed something.

**Some of this documentation may be outdated, exploration of the library is encouraged.**

---

# Gradle Dependency

[ ![jCenter](https://api.bintray.com/packages/drummer-aidan/maven/material-camera/images/download.svg) ](https://bintray.com/drummer-aidan/maven/material-camera/_latestVersion)
[![Build Status](https://travis-ci.org/afollestad/material-camera.svg)](https://travis-ci.org/afollestad/material-camera)
[![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg?style=flat-square)](https://www.apache.org/licenses/LICENSE-2.0.html)

The Gradle dependency is available via [jCenter](https://bintray.com/drummer-aidan/maven/material-camera/view).
jCenter is the default Maven repository used by Android Studio.

### Dependency

Add Bintray to your repositories, for some reason this specific library doesn't seem to work via jCenter
even though all of my other libraries do.

```gradle
repositories {
    jcenter()
    maven { url "https://dl.bintray.com/drummer-aidan/maven" }
}
```

Add this in your module's `build.gradle` file:

```gradle
dependencies {
    // ... other dependencies

    compile 'com.afollestad:material-camera:0.4.4'
}
```

---


# Basics

### Android Manifest

First, you have to register two library Activities from your app's `AndroidManifest.xml` file:

```xml
<activity
    android:name="com.afollestad.materialcamera.CaptureActivity"
    android:theme="@style/MaterialCamera.CaptureActivity" />
<activity
    android:name="com.afollestad.materialcamera.CaptureActivity2"
    android:theme="@style/MaterialCamera.CaptureActivity" />
```
            
Feel free to use your own custom theme. The included themes give the activities a good default look. 
See the sample project for more details.

### Code for Video

```java
private final static int CAMERA_RQ = 6969; 

File saveFolder = new File(Environment.getExternalStorageDirectory(), "MaterialCamera Sample");
if (!saveFolder.mkdirs())
    throw new RuntimeException("Unable to create save directory, make sure WRITE_EXTERNAL_STORAGE permission is granted.");

new MaterialCamera(this)                               // Constructor takes an Activity
    .allowRetry(true)                                  // Whether or not 'Retry' is visible during playback
    .autoSubmit(false)                                 // Whether or not user is allowed to playback videos after recording. This can affect other things, discussed in the next section.
    .saveDir(saveFolder)                               // The folder recorded videos are saved to
    .primaryColorAttr(R.attr.colorPrimary)             // The theme color used for the camera, defaults to colorPrimary of Activity in the constructor
    .showPortraitWarning(true)                         // Whether or not a warning is displayed if the user presses record in portrait orientation
    .defaultToFrontFacing(false)                       // Whether or not the camera will initially show the front facing camera
    .allowChangeCamera(true)                           // Allows the user to change cameras. 
    .retryExits(false)                                 // If true, the 'Retry' button in the playback screen will exit the camera instead of going back to the recorder
    .restartTimerOnRetry(false)                        // If true, the countdown timer is reset to 0 when the user taps 'Retry' in playback
    .continueTimerInPlayback(false)                    // If true, the countdown timer will continue to go down during playback, rather than pausing.
    .videoEncodingBitRate(1024000)                     // Sets a custom bit rate for video recording.
    .audioEncodingBitRate(50000)                       // Sets a custom bit rate for audio recording.
    .videoFrameRate(24)                                // Sets a custom frame rate (FPS) for video recording.
    .qualityProfile(MaterialCamera.QUALITY_HIGH)       // Sets a quality profile, manually setting bit rates or frame rates with other settings will overwrite individual quality profile settings
    .videoPreferredHeight(720)                         // Sets a preferred height for the recorded video output.
    .videoPreferredAspect(4f / 3f)                     // Sets a preferred aspect ratio for the recorded video output.
    .maxAllowedFileSize(1024 * 1024 * 5)               // Sets a max file size of 5MB, recording will stop if file reaches this limit. Keep in mind, the FAT file system has a file size limit of 4GB.
    .iconRecord(R.drawable.mcam_action_capture)        // Sets a custom icon for the button used to start recording
    .iconStop(R.drawable.mcam_action_stop)             // Sets a custom icon for the button used to stop recording
    .iconFrontCamera(R.drawable.mcam_camera_front)     // Sets a custom icon for the button used to switch to the front camera
    .iconRearCamera(R.drawable.mcam_camera_rear)       // Sets a custom icon for the button used to switch to the rear camera
    .iconPlay(R.drawable.evp_action_play)              // Sets a custom icon used to start playback
    .iconPause(R.drawable.evp_action_pause)            // Sets a custom icon used to pause playback
    .iconRestart(R.drawable.evp_action_restart)        // Sets a custom icon used to restart playback
    .labelRetry(R.string.mcam_retry)                   // Sets a custom button label for the button used to retry recording, when available
    .labelConfirm(R.string.mcam_use_video)             // Sets a custom button label for the button used to confirm/submit a recording
    .autoRecordWithDelaySec(5)                         // The video camera will start recording automatically after a 5 second countdown. This disables switching between the front and back camera initially.
    .autoRecordWithDelayMs(5000)                       // Same as the above, expressed with milliseconds instead of seconds.
    .audioDisabled(false)                              // Set to true to record video without any audio.
    .start(CAMERA_RQ);                                 // Starts the camera activity, the result will be sent back to the current Activity
```

**Note**: For `retryExists(true)`, `onActivityResult()` in the `Activity` that starts the camera will
receive `MaterialCamera.STATUS_RETRY` as the value of the `MaterialCamera.STATUS_EXTRA` intent extra.

---

# Length Limiting

You can specify a time limit for recording. `countdownMillis(long)`, `countdownSeconds(float)`, 
and `countdownMinutes(float)` are all methods for length limiting.

```java
new MaterialCamera(this)
    .countdownMinutes(2.5f)
    .start(CAMERA_RQ);
```

When the countdown reaches 0, recording stops. There are different behaviors that can occur after this based on
`autoSubmit` and `autoRetry`:

1. `autoSubmit(false)`, `allowRetry(true)`
    * The user will be able to playback the recording, and the 'Retry' button will be visible. This is default behavior.
2. `autoSubmit(false)`, `allowRetry(false)`
    * The user will be able to playback the recording, but the 'Retry' button will be hidden.
3. `autoSubmit(true)`, `allowRetry(false)`
    * The user won't be able to playback the recording, the result will immediately be returned to the starting Activity.
4. `autoSubmit(true)`, `allowRetry(true)`
    * If you don't specify a length limit, the behavior will be the same as number 3. If you do specify a length limit, the user is allowed to retry, but the countdown timer will continue until it reaches 0. When the countdown is complete, the result will be returned to the starting Activity automatically.

If you want the countdown to start immediately when the camera is open, as opposed to when the user presses
'Record', you can set `countdownImmediately(true)`:

```java
new MaterialCamera(this)
    .countdownMinutes(2.5f)
    .countdownImmediately(true)
    .start(CAMERA_RQ);
```

---

### Code for Stillshots (Pictures)

```java
new MaterialCamera(this)
    /** all the previous methods can be called, but video ones would be ignored */
    .stillShot() // launches the Camera in stillshot mode
    .start(CAMERA_RQ);
```
---

# Receiving Results

```java
public class MainActivity extends AppCompatActivity {

    private final static int CAMERA_RQ = 6969;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        new MaterialCamera(this)
            .start(CAMERA_RQ);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        // Received recording or error from MaterialCamera
        if (requestCode == CAMERA_RQ) {
        
            if (resultCode == RESULT_OK) {
                Toast.makeText(this, "Saved to: " + data.getDataString(), Toast.LENGTH_LONG).show();
            } else if(data != null) {
                Exception e = (Exception) data.getSerializableExtra(MaterialCamera.ERROR_EXTRA);
                e.printStackTrace();
                Toast.makeText(this, e.getMessage(), Toast.LENGTH_LONG).show();
            }
        }
    }
}
```

---

# [LICENSE](/LICENSE.md)

###### Copyright 2016 Aidan Follestad

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
