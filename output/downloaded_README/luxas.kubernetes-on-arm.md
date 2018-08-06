## Welcome to the Kubernetes on ARM project!

#### Kubernetes on a Raspberry Pi? Is that possible?

#### Yes, now it is (and has been since v1.0.1 with this project)
Imagine... Your own testbed for Kubernetes with cheap Raspberry Pis and friends. 

![Image of Kubernetes and Raspberry Pi](docs/raspberrypi-joins-kubernetes.png)

#### **Are you convinced too, like me, that cheap ARM boards and Kubernetes is a match made in heaven?**    
**Then, lets go!**

## Important information

This project was published in September 2015 as the first fully working way to easily set up Kubernetes on ARM devices.

You can read my story [here](https://www.cncf.io/blog/2016/11/29/diversity-scholarship-series-programming-journey-becoming-kubernetes-maintainer).

I worked on making it better non-stop until early 2016, when I started contributing the changes I've made back to Kubernetes core.
I strongly think that most of these features belong to the core, so everyone may take advantage of it, and so Kubernetes can be ported to even more platforms.

So I opened [kubernetes/kubernetes#17981](https://github.com/kubernetes/kubernetes/issues/17981) and started working on making Kubernetes cross-platform.
To date I've ported the Kubernetes core to ARM, ARM 64-bit and PowerPC 64-bit Little-endian. Already in `v1.2.0`, binaries were released for ARM, and I used the official binaries in `v0.7.0` in Kubernetes on ARM.

Since `v1.3.0` the `hyperkube` image has been built for both `arm` and `arm64`, which have made it possible to run Kubernetes officially the "kick the tires way".
So it has been possible to run `v1.3.x` Kubernetes on Raspberry Pi´s (or whatever arm or arm64 device that runs docker) with the [docker-multinode](https://github.com/kubernetes/kube-deploy/tree/master/docker-multinode) deployment.
However, docker-multinode has been [deprecated and removed](https://groups.google.com/forum/#!topic/kubernetes-dev/iBs-EBCQxq0), and shouldn'be be used anymore.

I've written a proposal about how to make Kubernetes available for multiple platforms [here](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/multi-platform.md)

Then I also ported `kubeadm` to `arm` and `arm64`, and `kubeadm` is so much better than the docker-multinode deployment method I used earlier (before the features that kubeadm takes advantage of existed).

So now the officially recommended and supported way of running Kubernetes on ARM is by following the [`kubeadm getting started guide`](http://kubernetes.io/docs/getting-started-guides/kubeadm/).
Since I've moved all the features this project had into the core, there's no big need for this project anymore.

### Get your ARM device up and running Kubernetes in less than ten minutes

I have a workshop how to create a Kubernetes cluster on ARM here now: https://github.com/luxas/kubeadm-workshop.
Please look there for information how to create a Kubernetes cluster on ARM or look at the [`kubeadm getting started guide`](http://kubernetes.io/docs/getting-started-guides/kubeadm/).

### Various related resources

 - https://www.youtube.com/watch?v=ZdzKQwMjg2w
 - http://slides.com/lucask/kubecon-berlin
 - https://github.com/luxas/kubeadm-workshop
 - http://blog.kubernetes.io/2017/01/stronger-foundation-for-creating-and-managing-kubernetes-clusters.html
 - https://luxaslabs.com/2016/12/31/2016-a-year-of-being-a-member-in-an-open-source-community/
 - https://twitter.com/kubernetesonarm
 - https://opensource.com/article/17/3/kubernetes-raspberry-pi
 - http://blog.hypriot.com/post/setup-kubernetes-raspberry-pi-cluster/
