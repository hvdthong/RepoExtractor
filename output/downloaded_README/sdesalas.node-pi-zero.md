![Node Pi Zero](https://raw.githubusercontent.com/sdesalas/node-pi-zero/eb55d80c724950137b79dbeded540789dc3cf455/pizero.png)

# node-pi-zero

Use the commands below to install node in the Raspberry Pi Zero.

They are re-runnable so you can upgrade or downgrade just by running the command for each version.

## v4.0.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v4.0.0.sh | bash
```

## v4.4.1

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v4.4.1.sh | bash
```

## v4.7.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v4.7.0.sh | bash
```

## v4.8.7

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v4.8.7.sh | bash
```

## v5.0.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v5.0.0.sh | bash
```

## v5.12.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v5.12.0.sh | bash
```

## v6.0.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v6.0.0.sh | bash
```

## v6.4.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v6.4.0.sh | bash
```

## v6.9.1

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v6.9.1.sh | bash
```

## v6.11.3

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v6.11.3.sh | bash
```

## v6.13.1

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v6.13.1.sh | bash
```

## v7.2.1

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v7.2.1.sh | bash
```

## v7.7.1

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v7.7.1.sh | bash
```

## v8.4.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.4.0.sh | bash
```

## v8.5.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.5.0.sh | bash
```

## v8.6.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.6.0.sh | bash
```

## v8.7.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.7.0.sh | bash
```

## v8.8.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.8.0.sh | bash
```

## v8.8.1

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.8.1.sh | bash
```

## v8.9.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.9.0.sh | bash
```

## v8.10.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v8.10.0.sh | bash
```

## v9.0.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v9.0.0.sh | bash
```

## v9.5.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v9.5.0.sh | bash
```

## v9.8.0

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v9.8.0.sh | bash
```

## v.lts

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v.lts.sh | bash
```

## v.last

```sh
$ wget -O - https://raw.githubusercontent.com/sdesalas/node-pi-zero/master/install-node-v.last.sh | bash
```

Looking for a specific version? The [following fork](https://github.com/Grayda/node-pi-zero) which has every version listed.

When finished just check the node and npm versions.

```sh
$ node -v
$ npm -v
```

## Using global npm modules? (ie mocha, eslint, etc)

Add the following to the end of your `~/.profile` file:
```sh
# Add support for node CLI tools
export PATH=$PATH:/opt/nodejs/bin
```

And remember, [friends dont let friends pipe to sh](https://www.seancassidy.me/dont-pipe-to-your-shell.html).
