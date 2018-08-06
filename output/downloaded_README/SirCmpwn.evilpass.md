# Slightly evil password strength checker

Checks how strong your user's password is via questionably ethical means.

![](https://sr.ht/sHst.gif)

## Usage

Please don't actually use this.

```python
>>> from evilpass import check_pass
>>> errors = check_pass("password", "email address", "username")
>>> errors
["Your password must be at least 8 characters long"]
```

## Password reuse is bad, okay?

So quit doing it. Use a password manager. I personally recommend
[pass](https://www.passwordstore.org/).

## Side note

If you're actually checking user's password strength on sign up, I strongly
suggest using an entropy-based strength estimation like [zxcvbn][]
instead of contrived composition rules like this, which are explicitly discouraged
by [NIST's current password guidelines][breakdown]. I also
suggest not trying to log into your user's account on other sites.

[zxcvbn]: https://github.com/dropbox/zxcvbn
[breakdown]: https://www.iansresearch.com/insights/blog/blog-insights/2016/08/24/ians-faculty-break-down-nist-s-proposed-new-password-guidelines

## Future development

* Automate use of proxies to avoid rate limiting and other things external
  services might do when they detect you're doing this
* Add other external services to check
* ~~Store valid credentials in a database for evil purposes~~

https://www.xkcd.com/792/
