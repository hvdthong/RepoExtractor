# DevCamp

Contains content for the Azure EDU partner DevCamp world tour

> The current status is:
>
>   **Worldwide deliveries in progress**
>
> Next update scheduled for January 2018

These labs and content will kickstart your Azure knowledge with a combination of lectures and hands on labs. It is intended to be delivered in a classroom environment but feel free to reuse this content.

----

## Module 0 - Introduction, roadmap and course overview

In this session, we will provide a brief history of Azure, a quick overview of the capabilities available and introduction to the 2-day interactive workshop.

[View PowerPoint](Presentation/Module00-Introduction.pptx?raw=true)

----

## [Hands on Labs overview](HOL/README.md)

This provides an overview of each hands on lab exercise.

----

## Module 1 - Tools and Developer Environment Setup Overview

We will provide an overview of the developer tools available for developing on your platform.

#### View [PowerPoint](Presentation/Module01-DevTools.pptx?raw=true)

### HOL 1: Setting up your developer environment

Setting up your developer environment for your specific language
In this lab you will create the environment that is needed for your language preference.

* Create O365 Developer Tenant
* Connect an Azure subscription (Trial or other)
* Take prepared image, walk through the tools that are available for your platform (.NET, Node.JS, Java | Windows, MacOSX)
* Run a custom ARM Template to scaffold out resources used during the training

#### View instructions for [.NET](HOL/dotnet/01-developer-environment) | [Node.JS](HOL/node/01-developer-environment) | [Java](HOL/java/01-developer-environment)

----

## Module 2 - Modern Cloud Apps Overview

We will provide an overview of some common cloud technologies, patterns and Azure features (Polyglot, scalability, app insights, Redis, patterns, traffic manager, global scale, blob, CDNs) and introduce you to the sample application. It is written 3-ways (.NET, Node.js and Java) so you can pick your platform of choice.

#### View [PowerPoint](Presentation/Module02-ModernCloudApps.pptx?raw=true)

### HOL 2: Building modern cloud apps

This lab will introduce you to building modern cloud apps with Azure. You will perform the following tasks:

* Connect to deployed API
* Add blob storage for the images
* Add queueing for image processing
* Add Redis cache for the dashboard
* Stretch: Image resizing with Azure Functions

#### View instructions for [.NET](HOL/dotnet/02-modern-cloud-apps) | [Node.JS](HOL/node/02-modern-cloud-apps) | [Java](HOL/java/02-modern-cloud-apps)

----

##  Module 3 - Identity and Office365 APIs Overview

We will provide an overview of Azure AD, and discuss areas for integration with the Office 365 APIs.

#### View [PowerPoint](Presentation/Module03-Identity-0365Apis.pptx?raw=true)

----

### HOL 3: Identity with Azure AD and Office 365 APIs
This lab will introduce you to identity in Azure AD and the Microsoft Graph. You will perform the following tasks:

* Create AAD Application
* Add authentication to app
* Populate first & last name of the new incident form with from the Graph/token
* Add a user profile page with a graph API call to get user data
* Send an email via Graph on new incident creation
* Stretch: Add a calendar event on new incident creation

#### View instructions for [.NET](HOL/dotnet/03-azuread-office365) | [Node.JS](HOL/node/03-azuread-office365) | [Java](HOL/java/03-azuread-office365)

----

## Module 4 - DevOps Overview

We will provide an overview of Visual Studio Team Services (VSTS), DevOps concepts, build tasks, release environments, integration with Azure and Git/GitHub and Azure to create a cross-platform build, integration and release pipelines.

#### View [PowerPoint](Presentation/Module04-DevOps.pptx?raw=true)

----

### HOL 4: DevOps with Azure and VSTS

This lab will introduce you to DevOps with Visual Studio Team Services. You will perform the following tasks:

* Create Visual Studio Team Services (VSTS) Online account
* Create Git repository
* Clone Git repo locally
* Push code into VSTS
* Create CI pipeline for build. Ends with published artifacts

#### View instructions for [.NET](HOL/dotnet/04-devops-ci) | [Node.JS](HOL/node/04-devops-ci) | [Java](HOL/java/04-devops-ci)

----

## Module 5 - Infrastructure as code with Azure Resource Manager (ARM)

Intro to Azure Resource manager and infrastructure as code.

#### View [PowerPoint](Presentation/Module05-ARM-IAC.pptx?raw=true)

### HOL 5: Infrastructure as code with (ARM)
This lab will introduce you to ARM templates and deployments to Azure. You will perform the following tasks:

* Create ARM template for web app in VS
* Deploy using VSTS
* Create 1 Production environment
* Configure Continuous deployment

#### View instructions for [.NET](HOL/dotnet/05-arm-cd) | [Node.JS](HOL/node/05-arm-cd) | [Java](HOL/java/05-arm-cd)

----

## Module 6 - Monitoring

We will introduce you to the monitoring capabilities in Azure and show you how you can use them in your application.

#### View [PowerPoint](Presentation/Module06-Monitoring.pptx?raw=true)

### HOL 6: Monitoring applications with App Insights

This lab will introduce you to Azure Application Insights. You will perform the following tasks:

* Add App Insights resource to Azure
* Add App Insights to application server side
* Monitor the API call
* Add client side library
* Dashboard custom event to capture dashboard views
* Create availability test that test the dashboard
* Stretch - Create custom metric around the API call

#### View instructions for [.NET](HOL/dotnet/06-appinsights) | [Node.JS](HOL/node/06-appinsights) | [Java](HOL/java/06-appinsights)

----

## Module 7 - Cognitive Services and the BOT framework

In this module, we will provide an overview of Cognitive Services APIs and an introduction to the BOT framework.

#### View [PowerPoint](Presentation/Module07-Cognitive%20Services%20and%20the%20BOT%20framework.pptx?raw=true)

### HOL 7: Bots

In this hands-on lab, you will learn how to:

* Set up the developing environment to support the creation of bot applications.
* Create your own bot from scratch.
* Create your own bot using Azure Bot Service.
* Hosting your bot in Azure.

#### View instructions for [.NET](HOL/dotnet/07-bot) | [Node.JS](HOL/node/07-bot) | [Java](HOL/java/07-bot)

----

## Module 8 - Analytics and PowerBI

We will provide a quick lap around the various APIs, features and services available for developers.

#### View [PowerPoint](Presentation/Module08-Analytics%20and%20PowerBI.pptx?raw=true)

### HOL 8 - Power BI

#### View instructions for [.NET](HOL/dotnet/08-PowerBI) | [Node.JS](HOL/node/08-PowerBI) | [Java](HOL/java/08-PowerBI)

### HOL 14: Machine Learning (IN DEVELOPMENT)

In this lab you will setup an Azure machine learning workspace and train a model to help predict the estimated time to resolution of logged incidents.

### View instructions for [.NET](HOL/dotnet/14-ML)

----

## Module 9 - IoT

In this module, you will learn about the Azure IoT capabilities and features.

#### View [PowerPoint](Presentation/Module09-IOT.pptx?raw=true)

### HOL 9: IoT

In this lab, you will combine the web app with an IoT device based on an Arduino-compatible board. You will perform the following tasks:

* Set up the developing environment to support the programming of Arduino chips.
* Create your own IoT software from scratch.

#### View instructions for [.NET](HOL/dotnet/11-IoT) | [Node.JS](HOL/node/11-IoT) | [Java](HOL/java/11-IoT)

### HOL 10: IoT using IoT Hub and containers (IN DEVELOPMENT)

In this lab you will setup an Azure IoT Hub, Create Devices, develop a .NET Core simulated device application, and deploy it as an Azure Container Instance.

### View instructions for [.NET](HOL/dotnet/12-IoTHub-ACI)

----

## Module 10 - Cloud Building Blocks

This module contains a short introduction to Containers, Cognitive Services, the Bot Framework and Skype for Business SDK.

#### View [PowerPoint](Presentation/Module10-Cloud%20Building%20Blocks.pptx?raw=true)

----

## Stretch Goal

This lab represents an optional stretch goal exercise where you add an additional feature to the City Power & Light sample application on your own.

In this hands-on lab, you will be using the knowledge gained in HOL 3 and learn about some additional Microsoft Graph features.

#### View instructions for [.NET](HOL/dotnet/10-stretch-goal) | [Node.JS](HOL/node/10-stretch-goal) | [Java](HOL/java/10-stretch-goal)
