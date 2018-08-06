AliceBundle
===========

A [Symfony](http://symfony.com) bundle to manage fixtures with [nelmio/alice](https://github.com/nelmio/alice) and
[fzaninotto/Faker](https://github.com/fzaninotto/Faker).

The database support is done in [FidryAliceDataFixtures](https://github.com/theofidry/AliceDataFixtures). Check this
project to know which database/ORM is supported.

**Warning: this is the documentation for HautelookAliceBundle 2.0. If you want to check the documentation for 1.x, head
[this way](https://github.com/hautelook/AliceBundle/tree/1.x).**

[![Package version](https://img.shields.io/packagist/v/hautelook/alice-bundle.svg?style=flat-square)](https://packagist.org/packages/hautelook/alice-bundle)
[![Build Status](https://img.shields.io/travis/hautelook/AliceBundle/master.svg?style=flat-square)](https://travis-ci.org/hautelook/AliceBundle?branch=master)
[![SensioLabsInsight](https://img.shields.io/sensiolabs/i/d93a3fc4-3fe8-4be3-aa62-307f53898199.svg?style=flat-square)](https://insight.sensiolabs.com/projects/d93a3fc4-3fe8-4be3-aa62-307f53898199)
[![Dependency Status](https://www.versioneye.com/user/projects/55d26478265ff6001a000084/badge.svg?style=flat)](https://www.versioneye.com/user/projects/55d26478265ff6001a000084)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/hautelook/AliceBundle.svg?style=flat-square)](https://scrutinizer-ci.com/g/hautelook/AliceBundle/?branch=master)
[![Code Coverage](https://img.shields.io/scrutinizer/coverage/g/hautelook/AliceBundle.svg?b=master&style=flat-square)](https://scrutinizer-ci.com/g/hautelook/AliceBundle/?branch=master)
[![Slack](https://img.shields.io/badge/slack-%23alice--fixtures-red.svg?style=flat-square)](https://symfony-devs.slack.com/shared_invite/MTYxMjcxMjc0MTc5LTE0OTA3ODE4OTQtYzc4NWVmMzRmZQ)


## When to use this bundle?

HautelookAliceBundle changed a lot, it first was acting as a simple bundle for [nelmio/alice](https://github.com/nelmio/alice),
it then started to ship some additional features to enrich it.

HautelookAliceBundle 1.x was the first milestone reaching a certain level of maturity in its usage:

- Easily load a set of fixtures from a command
- Being able to define different sets of fixtures for multiple environments
- Customize the data generation with custom Faker providers
- Customize the loading behaviour with processors

HautelookAliceBundle 2.x changes a lot, although not so much. In 1.x, a lot of complexity was brought in the bundle
due to nelmio/alice 2.x limitations and were at best workarounds (like the lack of handling of circular references).
A lot of that complexity has been pushed back to nelmio/alice 3.x which has a much more flexible design. As a result:

- [nelmio/alice](https://github.com/nelmio/alice) 3.x allows you to easily create PHP objects with random data in an elegant way
- [FidryAliceDataFixtures](https://github.com/theofidry/AliceDataFixtures) is a persistence layer for nelmio/alice 3.x. If you need to persist the loaded objects,
  it is the package you need. It provides you the flexibility to be able to purge the data between each loadings or
  wrap the loading in a transaction for your tests for example to simply rollback once the test is finished instead of
  calling an expansive purge.
- hautelook/alice-bundle 2.x is now only focused on the fixture discovery: find the appropriate files and load them. If
  you need to load specific sets of files for your tests, [FidryAliceDataFixtures](https://github.com/theofidry/AliceDataFixtures) is enough.


## Documentation

1. [Install](#installation)
1. [Basic usage](#basic-usage)
1. [Advanced usage](doc/advanced-usage.md)
    1. [Enabling databases](doc/advanced-usage.md#enabling-databases)
    1. [Environment specific fixtures](doc/advanced-usage.md#environment-specific-fixtures)
    1. [Fixtures parameters](doc/advanced-usage.md#fixtures-parameters)
        1. [Alice parameters](doc/advanced-usage.md#alice-parameters)
        1. [Application parameters](doc/advanced-usage.md#application-parameters)
    1. [Use service factories](doc/advanced-usage.md#use-service-factories)
    1. [Load fixtures in a specific order](doc/advanced-usage.md#load-fixtures-in-a-specific-order)
        1. [Load fixtures in a specific order](doc/advanced-usage.md#ordering-the-files-found)
        1. [Persisting the classes in a specific order](doc/advanced-usage.md#persisting-the-classes-in-a-specific-order)
1. [Custom Faker Providers](doc/faker-providers.md)
1. [Custom Alice Processors](doc/alice-processors.md)
1. [Resources](#resources)

Other references:

* [Knp University screencast](https://knpuniversity.com/screencast/alice-fixtures)


## Installation

Example of installation:

```bash
# If you are using Symfony standard edition, you can skip this step
composer require doctrine/doctrine-bundle doctrine/orm:^2.5

composer require --dev hautelook/alice-bundle doctrine/data-fixtures
```

Explanation: HautelookAliceBundle uses [FidryAliceDataFixtures](https://github.com/theofidry/AliceDataFixtures) for the
persistence layer. As FidryAliceDataFixtures is compatible with different databases/ORM, one cannot be installed by
default. In the example above, we are using Doctrine ORM which requires
`doctrine/orm doctrine/orm-bundle doctrine/data-fixtures`.

Then, enable the bundle by updating your `app/AppKernel.php` file to enable the bundle:

```php
<?php
// app/AppKernel.php

public function registerBundles()
{
    $bundles = [
        new Symfony\Bundle\FrameworkBundle\FrameworkBundle(),
        // ...
        new Doctrine\Bundle\DoctrineBundle\DoctrineBundle(),
    ];
    
    if (in_array($this->getEnvironment(), ['dev', 'test'])) {
        //...
        $bundles[] = new Nelmio\Alice\Bridge\Symfony\NelmioAliceBundle();
        $bundles[] = new Fidry\AliceDataFixtures\Bridge\Symfony\FidryAliceDataFixturesBundle();
        $bundles[] = new Hautelook\AliceBundle\HautelookAliceBundle();
    }

    return $bundles;
}
```

Configure the bundle to your needs (example with default values):

```yaml
# app/config/config_dev.yml

hautelook_alice:
    fixtures_path: 'Resources/fixtures' # Path to which to look for fixtures relative to the project directory or the bundle path.
    root_dirs:
        - '%kernel.root_dir%'
        - '%kernel.project_dir%'
```


## Basic usage

Assuming you are using [Doctrine](http://www.doctrine-project.org/projects/orm.html), make sure you
have the [`doctrine/doctrine-bundle`](https://github.com/doctrine/DoctrineBundle) and
[`doctrine/data-fixtures`](https://github.com/doctrine/data-fixtures) packages installed.

Then create a fixture file in one of the following location:

- `Resources/fixtures` if you are using flex
- `app/Resources/fixtures` if you have a non-flex bundle-less Symfony application
- `src/AppBundle/Resources/fixtures` or any bundle under which you want to place the fixtures

```yaml
# Resources/fixtures/dummy.yml

AppBundle\Entity\Dummy:
    dummy_{1..10}:
        name: <name()>
        related_dummy: '@related_dummy*'
```

```yaml
# Resources/fixtures/related_dummy.yml

AppBundle\Entity\RelatedDummy:
    related_dummy_{1..10}:
        name: <name()>
```

Then simply load your fixtures with the doctrine command `php bin/console hautelook:fixtures:load`.

If you want to load the fixtures of a bundle only, do `php bin/console hautelook:fixtures:load -b MyFirstBundle -b MySecondBundle`.

[See more](#documentation).<br />
Next chapter: [Advanced usage](doc/advanced-usage.md)


## Resources

* Behat extension: [AliceBundleExtension](https://github.com/theofidry/AliceBundleExtension)
* Bundle for generating AliceBundle compatible fixtures directly from Doctrine entities: [AliceGeneratorBundle](https://github.com/trappar/AliceGeneratorBundle)
* [Upgrade guide](UPGRADE.md)
  * [Upgrade from 0.X to 1.X](UPGRADE.md#from-0x-to-1x)
* [Changelog](CHANGELOG.md)


## Credits

This bundle was originaly developped by [Baldur RENSCH](https://github.com/baldurrensch) and [HauteLook](https://github.com/hautelook). It is now maintained by [Théo FIDRY](https://github.com/theofidry).

[Other contributors](https://github.com/hautelook/AliceBundle/graphs/contributors).


## License

[![license](https://img.shields.io/badge/license-MIT-red.svg?style=flat-square)](LICENSE)
