# Brave iOS Browser 

Download in the [App Store](https://itunes.apple.com/app/brave-web-browser/id1052879175?mt=8)

Brave is based on Firefox iOS, most of the Brave-specific code is in the [brave dir](brave/)

### Adding Brave to your app to open links

Either ensure your app supports [opening urls in a share menu](https://github.com/brave/browser-ios/wiki) or use this project https://github.com/brave/ios-open-thirdparty-browser to open links directly.

## Setup

<strong> 1. Install [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12) from the AppStore </strong>

<strong> 2. Install the latest LTS version of [Node.js](https://nodejs.org/en/download/) </strong>

<strong> 3. Install Homebrew: </strong>
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
<strong> 4. Install Carthage: </strong>
```
brew install carthage
```

<strong> 5. Download the source code: </strong>
```
git clone https://github.com/brave/browser-ios.git # this will download git if it isn't currently installed
```

<strong> 6. Run the following commands: </strong>
```
cd browser-ios
./checkout.sh # this pulls Carthage dependencies
(cd brave && ./setup.sh your.fake.appid) # put in a fake unique app id if you want to build to device
open Client.xcodeproj
```

#### Note: building your own ad-hoc builds is supported [see user device build](brave/docs/USER-DEPLOYING.md)
You will need a Apple developer account to run on your device.


## Crash reporting using Fabric

To enable, add ~/.brave-fabric-keys with 2 lines, the API key and build secret. Re-run setup.sh and the project will be generated to use Fabric and Crashlytics frameworks.

## Tests

Run Product>Test in Xcode to do so. Not all Firefox tests are passing yet.

## Contribution Notes

Most of the code is in the brave/ directory. The primary design goal has been to preserve easy merging from Firefox iOS upstream, so hopefully code changes outside of that dir are minimal.

To find changes outside of brave/, look for #if BRAVE / #if !BRAVE (#if/#else/#endif is supported by Swift).

## Adding Carthage modules

1. Add line into Cartfile, run `carthage bootstrap` to update Cartfile.resolved
2. Verify that your new module has been added to Cartfile.resolved
3. Run `checkout.sh`
4. In the Xcode Project, go to Client target settings, open the `Build Phases` tab and add a line such as
```
$(SRCROOT)/Carthage/Build/iOS/FRAMEWORKNAME.framework
```

## Provisioning Profiles using a Team account

(This section doesn't apply to individual developer accounts, Xcode managed profiles seem to work fine in that case.)

Do not use 'Xcode managed profiles', there is no advantage to this, and debugging problems with that system is a dead end due to lack of transparency in that system. 

```brave/build-system/profiles``` has some handy scripts to download the adhoc or developer profiles and install them.

## JS Tips

For anyone working with JS in iOS native, I recommend running and debugging your JS in an attached JS console. (Not using an edit/compile/debug cycle in Xcode). When you run from Xcode any iOS web view in the simulator (or attached device), you can then attach from Safari desktop (the Develop menu), and you get a JS console to work in. 

We have various JS interpreters available: UIWebView, JavaScriptCore, and WKWebView.

The first is required if we are running JS on the web page, since we are using UIWebView. JavaScriptCore is a stand-alone JS engine that I believe is more up-to-date than UIWebView's. WKWebView will have the most modern JS engine, but requires instantiating a WKWebView for this purpose, which we would prefer to avoid as that is a heavy approach. UIWebView's JS engine is a few years old, and is quite primitive.

None of these are comparable to Safari iOS's JS engine, which is highly up-to-date in its capabilities but is not available to us.

## Release Builds

```brave/build-system/build-archive.sh``` does everything. When that completes, the Fabric app detects a new archive and asks to distribute to testers.

## Misc Tips

If you get the dreaded "Launch Services Error 0": open ~/Library/Logs/CoreSimulator/CoreSimulator.log for info

Go to the Brave app folder for the most recently run simulator:
```
cd ~/Library/Developer/CoreSimulator/Devices && cd `ls -t | head -1` && cd data/Containers/Data/Application && cd `find . -iname "*brave*" | head -1 | xargs -I{} dirname {}`
```
