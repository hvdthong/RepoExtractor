# CircleCI Images [![CircleCI Build Status](https://circleci.com/gh/circleci/circleci-images.svg?style=shield)](https://circleci.com/gh/circleci/circleci-images) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/circleci/circleci-docs/master/LICENSE) [![CircleCI Community](https://img.shields.io/badge/community-CircleCI%20Discuss-343434.svg)](https://discuss.circleci.com)

A set of convenience images that work better in context of CI.  This repo contains the official set of images that CircleCI maintains.  It contains language as well as services images:

* Language images (e.g. `ruby`, `python`, `node`) are images targeted for common programming languages with the common tools pre-installed.  They primarily extend the [official images](#official-images) and install additional tools (e.g. browsers) that we find very useful in context of CI.
* Service images (e.g. `mongo`, `postgres`) are images that have the services pre-configured with development/CI mode.  They also primarily extend the corresponding [official images](#official-images) but with sensible development/CI defaults (e.g. disable production checks, default to nojournal to speed up tests)

## Official Images

We extend [Docker Official Repositories](https://docs.docker.com/docker-hub/official_repos/) in order to start with the same consistent set of images.

This allows us to make things more standardized. From our scripts for checking for updates, the type of OS on the base image, and so forth. We can recommend using `apt-get install` rather than documenting various constraints depending on which stack you're using.

The official images on Docker Hub are curated by Docker as their way to provide convenience images which address both development and production needs. Since Docker sponsors a dedicated team responsible for reviewing each of the official images, we can take advantage of the community maintaining them independently without trying to track all of the sources and building automations for each one. For now we can take a shortcut, without building this infrastructure.

Finally, our convenience images are augmenting these official images, by adding some missing packages, that we install ourselves for common dependencies shared for the CI environment.

All of the official images on Docker Hub have an "_" for the username, for example:
https://hub.docker.com/_/ruby

You can view all of the officially supported images here:
https://hub.docker.com/explore/

CircleCI supported images are here:
https://hub.docker.com/r/circleci/

To view the Dockerfiles for CircleCI images, visit the [CircleCI-Public/circleci-dockerfiles](https://github.com/circleci-public/circleci-dockerfiles) repository.

# How to add a bundle with images

A bundle is a top-level subfolder in this repository (e.g. `postgres`).

For the image Dockerfiles, we use a WIP templating mechanism.  Each bundle should contain a `generate-images` script for generating the Dockerfiles.  You can use [`postgres/generate-images`](postgres/generate-images) and [`node/generate-images`](node/generate-images) for inspiration.  The pattern is executable script of the following sample:


```bash
#!/bin/bash

# the base image we should be tracking.  It must be a Dockerhub official repo
BASE_REPO=node

# Specify the variants we need to publish.  Language stacks should have a
# `browsers` variant to have an image with firefox/chrome pre-installed
VARIANTS=(browsers)

# By default, we don't build the alpine images, since they are typically not dev friendly
# and makes our experience inconsistent.
# However, it's reasonable for services to include the alpine image (e.g. psql)
#
# uncomment for services

#INCLUDE_ALPINE=true

# if the image needs some basic customizations, you can embed the Dockerfile
# customizations by setting $IMAGE_CUSTOMIZATIONS.  Like the following
#

IMAGE_CUSTOMIZATIONS='
RUN apt-get update && apt-get install -y node
'

# boilerplate
source ../shared/images/generate.sh
```

By default, the script uses `./shared/images/Dockerfile-basic.template` template which is most appropriate for language based images.  Language image variants (e.g. `-browsers` images that have language images with browsers installed) use the `./shared/images/Dockerfile-${variant}.template`.

Service image should have their own template.  The template can be kept in `<bundle-name>/resources/Dockerfile-basic.template` - like [`./mongo/resources/Dockerfile-basic.template`](./mongo/resources/Dockerfile-basic.template).

To build all images - push a commit with `[build-images]` text appearing in the commit message.

Also, add the bundle name to in Makefile `BUNDLES` field.

## Limitations
* The template language is WIP - it only supports `{{BASE_IMAGE}}` template.  We should extend this.
* Generated Dockerfiles isn't checked into repo.  Since we track moving set of tags, checking into repository can create lots of unnecessary changes.
* By default, the `master` branch of this repository pushes to the [`ccistaging` Docker Hub org](https://hub.docker.com/r/ccistaging).  Once we get some test builds with these images, we can promote them to the [`circleci` Docker Hub org](https://hub.docker.com/r/circleci) by merging changes from the `master` branch into the `production` branch.

## Licensing
The `circleci-images` repository is licensed under The MIT License. See [LICENSE](https://github.com/moby/moby/blob/master/LICENSE) for the full license text.
