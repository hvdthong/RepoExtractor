# Qactive
A reactive queryable observable framework.
<img align="right" src="https://raw.githubusercontent.com/RxDave/Qactive/master/Artifacts/Logo2.png" />

* **Runtime:** .NET Framework 4.6.1; 4.5.2 (portable); 4.0
* **Development:** Visual Studio 2017 and C# 7
* **Dependencies:** [Reactive Extensions (Rx.NET)](https://github.com/Reactive-Extensions/Rx.NET)

## Download from NuGet
> [Qactive.Providers.Tcp](https://www.nuget.org/packages/qactive.providers.tcp)  
> Depends on Rx, Qactive.Providers.Streaming, Qactive.Expressions and Qactive  
> Runtimes: .NET Framework 4.6.1; 4.5.2; 4.0

> [Qactive.Providers.Streaming](https://www.nuget.org/packages/qactive.providers.streaming)  
> Depends on Rx, Qactive.Expressions and Qactive  
> Runtimes: .NET Framework 4.6.1; 4.5.2; 4.0

> [Qactive](https://www.nuget.org/packages/qactive)  
> Depends on Rx  
> Runtimes: .NET Framework 4.6.1; 4.5.2; 4.0, ASP.NET Core 1.0, Windows 8, Windows Phone 8.1, Xamarin.Android, Xamarin.iOS

> [Qactive.Expressions](https://www.nuget.org/packages/qactive.expressions)  
> No dependencies  
> Runtimes: .NET Framework 4.6.1; 4.5.2; 4.0

## Overview
Qactive builds on Reactive Extension's queryable observable providers, enabling you to write elegant reactive queries in LINQ that execute server-side, even though they are written on the client.
Qactive makes the extremely powerful act of querying a reactive service as easy as writing a typical Rx query.

More specifically, Qactive enables you to easily expose `IQbservable<T>` services for clients to query. When a client defines a query and subscribes, a connection is made to the server and the 
serialized query is transmitted to the server as an expression tree. The server deserializes the expression tree and executes it as a standing query. Any output from the query is marshaled back 
to the client over a persistent, full-duplex connection. Members on closures and static members that are local to the client are invoked from within the service automatically via full-duplex 
messaging. Anonymous types are automatically serialized as well.

For more information, see [this series of blog posts](http://davesexton.com/blog/page/TCP-Qbservable-Provider-Series.aspx).

> **Warning:** Qactive allows clients to execute arbitrary code on your server.
> There are security mechanisms in place by default to prevent malicious clients but only to a point, 
> it hasn't been fully considered yet. Do not expose a Qbservable service on a public server without 
> taking the necessary precautions to secure it first.

> See [Security Guidelines](Artifacts/Security%20Guidelines.md) for more information.

## Features

Please refer to the [list of features](../../wiki/Features) in the wiki.

## Getting Started
Qactive is a set of .NET class libraries that you can reference in your projects. NuGet is recommended.

Add a reference to the **Qactive.Providers.Tcp** package in your Visual Studio project. That package references the other packages as dependencies, so NuGet will automatically download all of them for you.

> **Note:** Currently, the TCP provider is the only provider available.

The source code's [Examples](Examples/) folder contains projects that show various usages of Qactive, from a simple query over a timer to a real-time chat application.

### To run the examples:
1. Run _QbservableServer.exe_.
  1. The server will start hosting example Qbservable services as soon as the console application begins.
  1. Pressing a key at any time will stop the server.
1. Run _QbservableClient.exe_.
  1. You can run several client console applications at the same time.
1. When the client console application starts, press any key to connect to the server.  The client will begin running the first example.
1. Press any key to stop the current example and start the following example.

### To build the source code:
1. Set the *QbservableServer* project as the startup project.
1. Build and run. The server will start as soon as the console application begins.
1. Set the *QbservableClient* project as the startup project.
1. Build and run. You can run several client console applications at the same time.
1. When the client console application starts, press any key to connect to the server.

> **Tip:** To see the original and rewritten expression trees, run the client application with the debugger attached and look at the **Output** window.

## Simple Example
The following example creates a _cold_ observable sequence that generates a new notification every second and exposes it as an `IQbservable<long>` service over TCP port 3205 on the local computer.

### Server
```c#
IObservable<long> source = Observable.Interval(TimeSpan.FromSeconds(1));

var service = source.ServeQbservableTcp(new IPEndPoint(IPAddress.Loopback, 3205));

using (service.Subscribe(
  client => Console.WriteLine("Client shutdown."),
  ex => Console.WriteLine("Fatal error: {0}", ex.Message),
  () => Console.WriteLine("This will never be printed because a service host never completes.")))
{
  Console.ReadKey();
}
```
The following example creates a LINQ query over the `IQbservable<long>` service that is created by the previous example.  Subscribing to the query on the client causes the query to be serialized to the server and executed there.  In other words, the `where` clause is actually executed on the server so that the client only receives the data that it requested without having to do any filtering itself.  The client will receive the first six values, one per second.  The server then filters out the next 2 values - it does not send them to the client.  Finally, the remaining values are sent to the client until either the client or the server disposes of the subscription.

### Client
```c#
var client = new TcpQbservableClient<long>(new IPEndPoint(IPAddress.Loopback, 3205));

IQbservable<long> query =
  from value in client.Query()
  where value <= 5 || value >= 8
  select value;

using (query.Subscribe(
  value => Console.WriteLine("Client observed: " + value),
  ex => Console.WriteLine("Error: {0}", ex.Message),
  () => Console.WriteLine("Completed")))
{
  Console.ReadKey();
}
```
