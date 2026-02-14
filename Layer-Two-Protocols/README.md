This lab incoporates several Layer two protocols, namely: VTP protocol, DTP protocol and STP protocol.

Starting initial configuration with VLAN Trunking Protocol. VTP is a Cisco Proprietary Protocol that communicates the definition of Virtual Local Area Network. Switches were respectively confgured as sever and clients. VLANs used in this lab are configured in the Switch on VTP server mode, This increases the VTP revision number. This VLAN information are propagated across other switches removing the need to manually configure the rest of the Switch.

VPT advertisements are sent only over 802.1q, and ISL trunk ports, therefore all P2P link ports are configured as trunk. the rest of the Switch receives the advertisement and scubcribe to the VTP domain. 

Host ports are configured as access ports with each ports subscribing to a VLAN, However the trunk ports carries VLAN frames from all VLAN (1-1005). VTP V2 allows the extended VLAN range 1006 - 4094 in VTP Transparent mode. Access pots are they configured to use PortFast using the command "Spanning-Tree Portfast" to eliminate the down time from the STP Port States. BPDU gaurd activated on access ports to protect the network from unauthorised, unexpected connections.  
