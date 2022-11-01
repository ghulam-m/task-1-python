import psutil
import os


def network_adapter():
    addresses = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    available_networks = []
    for intface, addr_list in addresses.items():
        if any(getattr(addr, 'address').startswith("169.254") for addr in addr_list):
            continue
        elif intface in stats and getattr(stats[intface], "isup"):
            available_networks.append(intface)

    return available_networks


def disable_enabled_adapters(adapter):
    for adapters in adapter:
        os.system("netsh interface set interface " + adapters + " disabled")
        print(adapters + " has been disabled.")


def enable_disabled_adapters(adapter):
    for adapters in adapter:
        os.system("netsh interface set interface " + adapters + " enabled")
        print(adapters + " has been enabled.")


if __name__ == "__main__":
    networkAdapter = network_adapter()

    if networkAdapter:
        print("Network Adapter(s) present")
        for i in networkAdapter:
            print(i)
    else:
        print("No Network adapter present")

    disable_enabled_adapters(networkAdapter)

    enable_disabled_adapters(networkAdapter)

