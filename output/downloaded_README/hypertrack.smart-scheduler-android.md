# smart-scheduler-android

[![Build Status](https://travis-ci.org/hypertrack/smart-scheduler-android.svg?branch=master)](https://travis-ci.org/hypertrack/smart-scheduler-android) [ ![Download](https://api.bintray.com/packages/piyushgupta27/maven/smart-scheduler/images/download.svg) ](https://bintray.com/piyushgupta27/maven/smart-scheduler/_latestVersion) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/672a8b4b2bfc4f7d86c07e22a435515a)](https://www.codacy.com/app/piyushguptaece/smart-scheduler-android?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hypertrack/smart-scheduler-android&amp;utm_campaign=Badge_Grade) [![Android Arsenal](https://img.shields.io/badge/Android%20Arsenal-smart--scheduler-brightgreen.svg?style=flat)](https://android-arsenal.com/details/1/4755) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/licenses/MIT) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

A utility library for Android to schedule one-time or periodic jobs while your app is running. Currently, Android OS supports 3 types of scheduling APIs: `Handler`, `AlarmManager` and `JobScheduler`. The choice of one suitable API, the inflexibility of switching between them and the amount of boilerplate code required for setting up makes it difficult to use these APIs. 
Want to know more on this and wondering why you should prefer using this library over doing it yourself. Check out the [blog post](https://blog.hypertrack.io/?p=6713). 

[android-job](https://github.com/evernote/android-job) is a similar scheduling library, which unifies `AlarmManager`, `GcmNetworkManager` & `JobScheduler` APIs. But when it comes to implementing network dependent jobs for an interval less than `30sec` or implementing jobs while the device is in PowerSaver Mode, it is not able to schedule such jobs as required. This is where `smart-scheduler` library gives an advantage over `android-job`.

## Download

Download the [latest version](https://oss.sonatype.org/content/repositories/releases/io/hypertrack/smart-scheduler/) or grab via Gradle:

The library is available on `mavenCentral()` and `jcenter()`. In your module's `build.gradle`, add the following code snippet and run the gradle-sync.

```
dependencies {
    ...
    compile 'io.hypertrack:smart-scheduler:0.0.13'
    ...
}
```

If you didn't turn off the manifest merger from the Gradle build tools, then no further step is required to setup the library. Otherwise you manually need to add the permissions and services like in this [AndroidManifest](https://github.com/hypertrack/smart-scheduler-android/blob/master/smart-scheduler/src/main/AndroidManifest.xml). 

## Usage

![Demo App](http://i.imgur.com/X53klUZ.gif?1)

* The class `SmartScheduler` serves as the entry point. You need to create a `Job` object with the corresponding job parameters using the `Job.Builder` class.

* The `Job.Builder` class has many extra options, e.g. you can specify a required network connection, required charging state, make the job periodic or run the job at an exact time.

```
	SmartScheduler.JobScheduledCallback callback = new SmartScheduler.JobScheduledCallback() {
        @Override
        public void onJobScheduled(Context context, Job job) {
            // Handle onJobScheduled here
        }
    };

    Job.Builder builder = new Job.Builder(JOB_ID, callback, jobType, JOB_PERIODIC_TASK_TAG)
            .setRequiredNetworkType(networkType)
            .setRequiresCharging(requiresCharging)
            .setIntervalMillis(intervalInMillis);

    if (isPeriodic) {
        builder.setPeriodic(intervalInMillis);
    }

    Job job = builder.build();
```

* Each job has a unique ID. This ID helps to identify the job later to update requirements or to cancel the job. In case this unique ID is not specified in the `Job` object, one will be auto-generated using `Job.generateJobID()` method.

* Once a `Job` object has been created with the relevant parameters, you can add this job using `SmartScheduler` class.

```
	SmartScheduler jobScheduler = SmartScheduler.getInstance(getApplicationContext());
    boolean result = jobScheduler.addJob(job);

    if (result) {
        // Job successfully added here
    }
```

* A `Non-Periodic` Job will be removed automatically once it has been scheduled successfully. For `Periodic` Jobs, call `SmartScheduler.removeJob(jobID)` method to remove the job.

```
	SmartScheduler jobScheduler = SmartScheduler.getInstance(getApplicationContext());
    boolean result = jobScheduler.removeJob(JOB_ID);

	if (result) {
        // Job successfully removed here
    }
``` 

## Utility Methods

* To check if a job (periodic or non-periodic) is currently scheduled for a given jobID, call `SmartScheduler.contains(jobID)` method as depicted below. This method returns `true` in case a `Job` is currently scheduled for the given `jobID`, `false` otherwise.

```
    SmartScheduler jobScheduler = SmartScheduler.getInstance(getApplicationContext());
    boolean result = jobScheduler.contains(JOB_ID);
    
	if (result) {
        // Job currently scheduled
    }    
```

* To get a scheduled Job for a given jobID, call `SmartScheduler.get(jobID)` method as depicted below. This method returns a `Job` object for the given `jobID` in case one is currently scheduled, `null` otherwise.

```
    SmartScheduler jobScheduler = SmartScheduler.getInstance(getApplicationContext());
    Job scheduledJob = jobScheduler.get(JOB_ID);
    
	if (scheduledJob != null) {
        // Valid job has been scheduled for given jobID
    }    
```

## Contribute
Please use the [issues tracker](https://github.com/hypertrack/smart-scheduler-android/issues) to raise bug reports and feature requests. We'd love to see your pull requests, so send them in!

## About HyperTrack
Developers use HyperTrack to build location features, not infrastructure. We reduce the complexity of building and operating location features to a few APIs that just work.
Check it out. [Sign up](https://dashboard.hypertrack.com/signup/) and start building! Join our [Slack community](http://slack.hypertrack.io) for instant responses. You can also email us at help@hypertrack.io

## License

```
MIT License

Copyright (c) 2016 HyperTrack

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
