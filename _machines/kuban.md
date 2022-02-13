---
layout: single
permalink: /machines/kuban/
title: "Kuban"
excerpt: "Supreme"
header:
  overlay_image: /assets/images/kuban2.jpg
  image: /assets/images/kuban2.jpg
  teaser: assets/images/kuban1.jpg
sidebar:
  nav: "machines"
---
* __Producer:__ [Kuban](https://kubancoffeeroasters.com/){:target="_blank"}, Turkey
* __Machines:__ Kuban Supreme (Automatic and Manual)
* __Connection:__ Siemens S7 via the network or MODBUS RTU via USB
* __Features:__
  - logging of environmental temperature (ET), bean temperature (BT) and related rate-of-rise curves
  - additional the Supreme Automatic allows logging and control of drum speed, fan speed, burner power and mixer speed
 
<figure>
<center>
<a href="{{ site.baseurl }}/assets/images/buttons-kuban.png">
<img src="{{ site.baseurl }}/assets/images/buttons-kuban.png" style="width: 80%;"></a>
    <figcaption>custom event buttons</figcaption>
</center>
</figure>
 
### Setup Supreme Automatic

The computer running Artisan must be on the same IP network as the roaster. The default IP address of the roaster is 192.168.0.5. Configure your computer to use a static IP address in the range of the roaster (192.168.0.x) but with x different from that of the roaster (eg. 192.168.0.42). Choose 255.255.255.0 as subnet mask. 
 
This can be done on Windows using the Network Sharing Center by adding a TCP/IPv4 Local Area Connection with those properties. On macOS you set your ethernet port in the Network Control panel to "IPv4: Manually" and fill in the IP and subnet mask accordingly.

**Watch out!** Artisan doesn't monitor unsafe temperatures, so you should never leave the roaster alone.
{: .notice--primary}