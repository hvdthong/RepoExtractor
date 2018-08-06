<p align="center">
    <a href="http://cierge.biarity.me" target="_blank">
    <img alt="Cierge" title="Cierge" src="https://github.com/PwdLess/Cierge-Website/blob/master/Design/LogoBlack.png?raw=true" width="500">
    </a>
</p>
<p align="center">
Cierge is an OpenID Connect server that <b>handles user signup, login, profiles, management, social logins, and more.</b><br>
Instead of storing passwords, Cirege uses <b>magic links/codes and external logins</b> to authenticate your users.
<br />

</p>

<a href="https://cierge.azurewebsites.net" target="_blank"><h3><b>🔑Try out a demo</b></h3></a>

<a href="http://cierge.biarity.me" target="_blank"><h4>🌐Homepage</h4></a>

<a href="https://biarity.gitlab.io/2018/02/23/passwordless" target="_blank"><h5>❓Why passwordless</h4></a>

[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/Biarity)

---

## Why Cierge 🗝️

### Tried & tested - Passwordless is the future

Passwords are [insecure](https://www.entrepreneur.com/article/246902)
 [by](https://www.wired.com/2012/11/ff-mat-honan-password-hacker/) [default](https://blog.codinghorror.com/password-rules-are-bullshit/). Cierge does away by the illusion of security passwords give ("forgot password" usually relies upon email-based auth at the end of the day).

### No passwords to hash, salt, store, protect, or worry about

Even if your database is compromised, your users won't be.

### Users won't have to come up with their 278th password

Lack of complex password rules means convenience for both you and your users. User won't have to come up with and remember yet another password, and you won't have to worry about password reuse.

### User management

Users can edit their profiles and add or remove emails or external logins while an admin manages it all from the admin panel.

### External logins out of the box

Instead of logging in using email, users can use social logins such as Google, Facebook, Github, etc. Users can also associate multiple logins for one account. External logins are very easy to setup, for example, to add Google logins simply paste your site key & secret into the configuration and Cierge does the rest!

### Fully Stateless

Cierge does not store the magic codes in a database. You can generate a code, turn Cierge off & delete all databases, then turn it back on and your token would still be valid if you made it before expiry.

### Use as an SSO

Since Cierge doesn't care about the rest of your tech stack, you can use the same Cierge server for multiple apps & share users. As a matter of fact, you can use the demo Cierge server for your own apps just fine!

### Invisible reCAPTCHA

Cierge utilizes invisible reCAPTCHA to ensure magic codes (which expire quickly) are not brute-forceable. The reCAPTCHA only appears after multiple wrong attempts at a 6-digit code. You can make this code longer or disable magic codes and use magic links exclusively if you want.

### No profile existence leakage. Actually, no leakage of any kind.

With traditional password systems, a malicious user can try to register with an email to find out if it exists. With Cierge, 0 data is leaked about users or if they exist - until authenticated. This comes naturally since Cierge makes little distinction between registration and login.

---

## FAQ ⁉️

**😟What if a user's email is compromised?**

That's also a problem with traditional password logins. An attacker can click "forgot password", enter an email, and simply bypass the password altogether. As a matter of fact, Cierge removes a point of failure by making passwordless the only login method.

**😲What if my email is only accessible on another device?**

Cierge sends a magic link as well as a magic code that a user can manually enter into the login screen to continue as an alternative to clicking the link. Magic codes are short, volatile, & memorable (eg. 443 863). For example, you can look up the code on your phone then enter it into your browser on desktop. Note that Cierge also allows external social logins so users can skip emails altogether.

**😫I don't find this convenient enough!**

Cierge supports external social logins (eg. Google, Facebook, Twitter, Github, etc.) in addition to email login. Users can use any number of login methods at the same time. Also remember that Cierge is, if anything, more convenient than the now-popular 2FA. 

**🤔How does Cierge handle changing emails?**

Cierge does not have a "change email" feature. Instead, users can "add" or "remove" logins (logins can be emails or external logins) - so changing an email is equivalent to adding a new email (which involves verifying it) then optionally removing the old one. This ensures users can't use unverified emails, and makes it hard for an intruder to completely take ownership of an account. Removing your last login is equivalent to deleting your account.

**🤔What about breach detection?**

With traditional password logins, a user would notice if their password has been changed. With Cierge, a user would notice if an attacker removed their email from their logins. In addition, Cierge exposes an easily-accessible read-only event log of everything that has happened to an account (with associated IP addresses & user agents) to aid in breach detection, accessible to account owners and admins.

**🤔What measures are in place to prevent an attacker from fully compromising an account?**

Cierge's next version will implement security lock periods for removing logins - for example: "an email login that has existed for at least 60 days will require at least 30 days to be removed, otherwise, it can be removed instantly". This will prevent an attacker from removing the user's email (and locking them out) whilst also preventing them from adding their own email. In addition, notification emails will be sent to the user whenever account settings have been changed.

**🤔What about email greylisting?**

Greylisting also affects passwordful systems. User emails *should always be verified* before allowing the user to do anything of significance. Cierge also supports external logins so using email is not a necessity.

**🤔Why does Cierge handle profile metadata?**

This allows Cierge to collect any must-have profile information from users when they register. You can easily define new fields for storage, but you'll have to work with Cierge's source.

---

## Deploying Cierge 🎢

Since Cierge is an ASP.NET Core project, you can easily deploy it on any platform (including Linux/Docker/Windows/Mac).
Just add your [configuration](#configuration-%EF%B8%8F) then deploy.

Guides:

* [ASP.NET Core deployment](https://docs.microsoft.com/en-us/aspnet/core/publishing/?tabs=aspnetcore2x)
* [Docker guide](https://docs.microsoft.com/en-us/aspnet/core/publishing/docker)
* [More on .NET Core deployment](https://docs.microsoft.com/en-us/dotnet/core/deploying/)

There is also a [sample Dockerfile](/Dockerfile). 
For a more complete example on how you'd use Cierge in a multicontianer docker project, check out [Docker Starter](https://github.com/Biarity/DockerStarter).

It is recommended that you run Cierge behind a reverse proxy that requires https and implements some form of [rate limiting](https://blog.codinghorror.com/rate-limiting-and-velocity-checking/).

---

## Configuration ⚙️

Cierge reads configuration from multiple sources, in this order (later overrides earlier):

* appsettings.json
* appsettings.\<Environment\>.json (`<Environment>` is either "Development" or "Production")
* Environment variables
* Command-line arguments

For more information on how Cierge reads configuration, check out the [ASP.NET Core 2.0 configuration docs](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?tabs=aspnetcore2x#tabpanel_OdIy7kBIBJ_aspnetcore2x).

Here's a walkthrough of the configuration required by Cierge:

(`ConnectionStrings:DefaultConnection`, `Recaptcha`, `Smtp`, & `Cierge:Audience` are the only required ones)
```
{
  "ConnectionStrings": {
    "DefaultConnection": `string: a PostgreSQL connection string.
	                 [Using a different database provider](https://docs.microsoft.com/en-us/ef/core/providers/).
			 Don't forget to apply database migrations [`dotnet ef database update`](https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/).`
  },
  "Recaptcha": {
    "Secret": `string: reCAPTCHA secret, required`,
    "SiteKey": `string: reCAPTCHA site key, required`
  },
  "ExternalAuth": {
    "Google": { // only fill these out if you want external Google logins
      "ClientId": `string`,
      "ClientSecret": `string`
    }
  },
  "Smtp": { // configuration for email sending
    "Host": `string`,
    "Username": `string`,
    "Password": `string`,
    "Ssl": `boolean: highly recommended`,
    "Port": `number`,
    "From": `string`,
    "RandomizeFrom": `boolean: allow addition of random characters before the @ symbol - see issue #18`
  },
  "Cierge": {
    "RsaSigningKeyJsonPath": `string: OIDC RSA signing json key path (see RsaKeyGenerator), optional, leave empty to generate`,
    "Issuer": `string: OIDC issuer, optional, useful if running behind reverse proxy or using JWTs`,
    "RequireHttps": `boolean: leave off if running behind reverse proxy`,
    "AppName": `string: name of your main website, cosmetic`,
    "AppUrl": `string: url of your main website, cosmetic`,
    "Audience": `string: "aud" claim in tokens, required",
    "BeNice": `boolean: display "Powered by Cierge"`,
    "Events": {
      "MaxStored": `number: maximum number of events stored (default 50)`,
      "MaxReturned": `number: maximum number of events displayed per user (default 10)`
    },
    "Logins": {
      "MaxLoginsAllowed": `number: maximum number of logins allowed per user (default 5)`
    }
  }
}
```

* To change the port, use the environment variable `ASPNETCORE_URLS`
* To pass hierarchical configuration via environment variables or command-line arguments, use a ":" (eg. "Cierge:AppName")

### Configuring OpenID Connect

Cierge uses [OpenIddict](https://github.com/openiddict/openiddict-core) to provide all the OpenID Connect functionality (under the Implicit flow).

You can easily reconfigure OpenIddict by editing [/Cierge/Startup.cs](/Cierge/Startup.cs) or [/Cierge/Controllers/AuthorizationController.cs](/Cierge/Controllers/AuthorizationController.cs).

---

## More 📔

### Adding a new profile field/claim

In the demo, you can see a "Favourite Color" user property, demonstrating how you'd implement additional user metadata fields.
To add a new field, search for the text `FavColor` in Ceirge's source. Add analogous code for your custom field. 
You will find comments starting with `!! ADDING FIELD:` that explain why a certain line of code might exist.
Do not edit migration code (you won't find a comment there).
Don't forget to [add a migration & apply it](https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/) once you're done, to update the database.

### Supporting more external login providers

Check out the [ASP.NET Core external authentication guide](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/social/)

### Cierge vs Portier vs PwdLess

* Unlike PwdLess & Portier, Cierge handles user management, a variety of external logins, and a frontend (more like an SSO).
* Portier is an email-based authentication server that *only* handles authentication (ie. no user management). 
Cierge might progressively implement parts of the Portier spec as it develops for standradization.
* PwdLess is an API-only passwordless authentication server that does not implement OIDC, as such it is easier to pick up

### Get your Cierge project featured

Feel free to email `admin at biarity dot me` if you made a project that uses Cierge for authenitcation and want to get it listed here.

---

## Recommended Email Providers 📧

It is recommended that you use a well-known email provider to enhance deliverability. Here are some free ones:

* [MailJet](https://mailjet.com) (free 6k emails/month)
* [Mailgun](https://mailgun.com) (free 10k emails/month)
* [Sendgrid](https://sendgrid.com) (free 40k emails/month)
* [Elastic Email](https://elasticemail.com) (free 150k emails/month)

## Follow development 💻

You can follow Cierge development at [our GitHub project board](https://github.com/PwdLess/Cierge/projects/3). Or on [twitter](https://twitter.com/Biarity).

## License & Contributing 📝
Cierge is licensed under Apache 2.0. Cierge uses OpenIddict for OpenID Connect functionality, which is also licensed under Apache 2.0. Any contributions highly appreciated!
