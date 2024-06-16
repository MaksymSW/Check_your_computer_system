
# Check your computer system setting
import wmi
import multiprocessing
import os
import cpuinfo
import platform


def get_processor_name():
    return platform.uname()
system_info = get_processor_name()   
print(f"Machine:\t\t {system_info.machine}")
print(f"Platform processor:\t {system_info.processor}")


def get_name_cpu():
    return cpuinfo.get_cpu_info()     
cpu_name = get_name_cpu()['brand_raw']
print(f"CPU_NAME:\t\t {cpu_name}")


def get_os_info():
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    return f"OS Name:\t\t {os_info.Name.split('|')[0]}"
print(get_os_info())


# The first way to count a number of CPUs
def get_cpu_count():
    return os.cpu_count()
cpu = get_cpu_count()
print(f"Number of CPUs =:\t {cpu}")


# The second way to count a number of CPUs
def get_num_cpus():
    return multiprocessing.cpu_count()
num_cpus = get_num_cpus()
print(f"Number of CPUs =:\t {num_cpus}")


def get_ram_info():
    computer = wmi.WMI()
    ram_info = computer.Win32_ComputerSystem()[0]
    ram_b = (float(ram_info.TotalPhysicalMemory))
    ram_gb = round((ram_b / 1024 ** 3))
    return f"Memory RAM =:\t\t {ram_gb}GB"
print(get_ram_info())

