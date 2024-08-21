import mysql.connector
from dotenv import load_dotenv
import os

def load_db():
    load_dotenv() # Loads (currently on local device) environment variables for security
    db = mysql.connector.connect(
        host="104.238.215.106",
        user="root",
        password="Huffmand3coding"
    )
    return db

### Initialize data about machine in db ###
def hello_entry(json: dict):
    if 'hello' in json.keys():
        db = load_db()
        cursor = db.cursor()

        ### Conditional creation of machines database ###
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS machines;"
        )
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS net_interfaces;"
        )
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS disks;"
        )
        cursor.execute( 
            "USE machines;"
        )

        ### General machine data ###
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS machines (
                    timestamp VARCHAR(50),
                    id VARCHAR(50),
                    os_type VARCHAR(30),
                    version_semantic VARCHAR(20),
                    edition VARCHAR(30),
                    bitness VARCHAR(10),
                    has_battery VARCHAR(10),
                    cpu_core_count INT,
                    cpu_thread_count INT,
                    clock_speed BIGINT,
                    ram_installed BIGINT,
                    gpu VARCHAR(100),
                    gpu_vram BIGINT,
                    max_frequency BIGINT,
                    PRIMARY KEY (`id`)
                );
            """
        )
        print(f"HELLO - ID: {json['id']}")
        print(f" - {json['hello']['os_type']}")
        print(f" - {str(json['hello']['version']['Semantic'])}")
        print(f" - {json['hello']['edition']}")
        print(f" - {json['hello']['bitness']}")
        print(f" - {str(json['hello']['battery']['has_battery'])}")
        print(f" - {json['hello']['cpu']['core_count']}")
        print(f" - {json['hello']['cpu']['thread_count']}")
        print(f" - {json['hello']['cpu']['clock_speed']}")
        print(f" - {json['hello']['ram']['installed']}")
        print(f" - {json['hello']['gpu']['name']}")
        print(f" - {json['hello']['gpu']['installed_vram']}")
        print(f" - {json['hello']['gpu']['max_frequency']}")

        cursor.execute(
            f"""INSERT IGNORE INTO machines (
                timestamp,
                id,
                os_type,
                version_semantic,
                edition,
                bitness,
                has_battery,
                cpu_core_count,
                cpu_thread_count,
                clock_speed,
                ram_installed,
                gpu,
                gpu_vram,
                max_frequency
            )
            VALUES (
                '{json['timestamp']}',
                '{json['id']}',
                '{json['hello']['os_type']}',
                '{str(json['hello']['version']['Semantic'])}',
                '{json['hello']['edition']}',
                '{json['hello']['bitness']}',
                '{str(json['hello']['battery']['has_battery'])}',
                '{json['hello']['cpu']['core_count']}',
                '{json['hello']['cpu']['thread_count']}',
                '{json['hello']['cpu']['clock_speed']}',
                '{json['hello']['ram']['installed']}',
                '{json['hello']['gpu']['name']}',
                '{json['hello']['gpu']['installed_vram']}',
                '{json['hello']['gpu']['max_frequency']}'
            );
            """
        )
        db.commit()
        cursor.close()
        db.close()

        ### Network Interfaces ###
        print("NETWORK INTERFACES")
        db = load_db()
        cursor = db.cursor()
        cursor.execute( 
            "USE net_interfaces;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}` (
                    id VARCHAR(50),
                    interface VARCHAR(25),
                    name VARCHAR(255),
                    description VARCHAR(255),
                    type VARCHAR(100),
                    ip VARCHAR(25),
                    PRIMARY KEY(interface)
                );
            """
        )
        db.commit()
        cursor.close()
        for network in json['hello']['network']['interfaces']:
            print(f" - {network}")
            cursor = db.cursor()
            cursor.execute(
                f"""
                INSERT IGNORE INTO `{json['id']}` (
                    id, 
                    interface, 
                    name, 
                    description, 
                    type, 
                    ip
                ) 
                VALUES (
                    '{json['id']}',
                    '{network}',
                    '{json['hello']['network']['interfaces'][network]['name']}',
                    '{json['hello']['network']['interfaces'][network]['description']}',
                    '{json['hello']['network']['interfaces'][network]['type']}',
                    '{json['hello']['network']['interfaces'][network]['ip_addresses'][0]}'
                );
                """
            )
            db.commit()
            cursor.close()

        ### Network Interfaces ###
        print("DISKS")
        db = load_db()
        cursor = db.cursor()
        cursor.execute( 
            "USE disks;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}` (
                    id VARCHAR(50),
                    disk VARCHAR(50),
                    type VARCHAR(50),
                    capacity BIGINT,
                    used BIGINT,
                    removable VARCHAR(15),
                    PRIMARY KEY(id)
                );
            """
        )
        db.commit()
        cursor.close()
        for disk in json['hello']['disk']['disks']:
            print(f" - {disk}")
            cursor = db.cursor()
            if "Unknown" in json['hello']['disk']['disks'][disk]['type']:
                disk_type = "Cloud"
            else:
                disk_type = json['hello']['disk']['disks'][disk]['type']
            cursor.execute(
                f"""INSERT IGNORE INTO `{json['id']}` (
                    id,
                    disk,
                    type,
                    capacity,
                    used,
                    removable
                ) 
                VALUES (
                    '{json['id']}',
                    '{disk}',
                    '{disk_type}',
                    '{json['hello']['disk']['disks'][disk]['capacity']}',
                    '{json['hello']['disk']['disks'][disk]['usage']}',
                    '{str(json['hello']['disk']['disks'][disk]['is_removable'])}'
                );
                """
            )
            db.commit()
            cursor.close()
        db.close()
        
### If machine is already in db ###
def checkin_entry(json: dict):
    print(f"ID: {json['id']}")
    db = load_db()
    cursor = db.cursor()
    ### BATTERY
    if 'battery' in json:
        print(" - BATTERY")
        print(f">> {json['battery']['percent']}")
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS battery;"
        )
        cursor.execute( 
            "USE battery;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}` (
                    timestamp VARCHAR(50),
                    id VARCHAR(50),
                    percentage INT
                );
            """
        )
        cursor = db.cursor()
        cursor.execute(
            f"""INSERT INTO `{json['id']}` (
                timestamp,
                id,
                percentage
            ) 
            VALUES (
                '{json['timestamp']}',
                '{json['id']}',
                '{json['battery']['percent']}'
            );
            """
        )
        db.commit()
        cursor.close()
        db.close()

    ### CPU ###
    elif 'cpu' in json:
        print(" - CPU")
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS cpu;"
        )
        cursor.execute( 
            "USE cpu;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}` (
                    timestamp VARCHAR(50),
                    id VARCHAR(50),
                    percent INT,
                    clock_speed BIGINT,
                    temperature BIGINT
                );
            """
        )
        if json['cpu']['current_temperature'] is None:
            json['cpu']['current_temperature'] = -1
        print(f">> {json['cpu']['usage_percent']}")
        print(f">> {json['cpu']['current_clock_speed']}")
        print(f">> {json['cpu']['current_temperature']}")
        cursor.execute(
            f"""INSERT INTO `{json['id']}` (
                timestamp,
                id,
                percent,
                clock_speed,
                temperature
            ) 
            VALUES (
                '{json['timestamp']}',
                '{json['id']}',
                '{json['cpu']['usage_percent']}',
                '{json['cpu']['current_clock_speed']}',
                '{json['cpu']['current_temperature']}'
            );
            """
        )
        db.commit()
        cursor.close()
        db.close()

    ### RAM ###
    elif 'ram' in json:
        print(" - RAM")
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS ram;"
        )
        cursor.execute( 
            "USE ram;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}` (
                    timestamp VARCHAR(50),
                    id VARCHAR(50),
                    ram_used BIGINT
                );
            """
        )
        print(f">> {json['ram']['usage']}")
        cursor.execute(
            f"""INSERT INTO `{json['id']}` (
                timestamp,
                id,
                ram_used
            ) 
            VALUES (
                '{json['timestamp']}',
                '{json['id']}',
                '{json['ram']['usage']}'
            );
            """
        )
        db.commit()
        cursor.close()
        db.close()

    ### net ###
    elif 'net' in json:
        print(" - NET")
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS net;"
        )
        cursor.execute( 
            "USE net;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}` (
                    timestamp VARCHAR(50),
                    mac VARCHAR(20),
                    name VARCHAR(50),
                    description VARCHAR(100),
                    net_type VARCHAR(25),
                    ip VARCHAR(15),
                    rx BIGINT,
                    tx BIGINT
                );
            """
        )
        for mac in json['net']['interfaces']:
            print(f">> {mac}")
            cursor.execute(
                f"""INSERT IGNORE INTO `{json['id']}` (
                    timestamp,
                    mac,
                    name,
                    description,
                    net_type,
                    ip,
                    rx,
                    tx
                ) 
                VALUES (
                    '{json['timestamp']}',
                    '{mac}',
                    '{json['net']['interfaces'][mac]['name']}',
                    '{json['net']['interfaces'][mac]['description']}',
                    '{json['net']['interfaces'][mac]['type']}',
                    '{json['net']['interfaces'][mac]["ip_addresses"][0]}',
                    '{json['net']['interfaces'][mac]["rx"]}',
                    '{json['net']['interfaces'][mac]["tx"]}'
                );
                """
            )
        db.commit()
        cursor.close()
        db.close()

    ### GPU ###
    elif 'gpu' in json:
        print(" - GPU")
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS gpu;"
        )
        cursor.execute( 
            "USE gpu;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}`(
                    timestamp VARCHAR(50),
                    id VARCHAR(50),
                    vram BIGINT,
                    frequency BIGINT,
                    temperature BIGINT
                );
            """
        )
        if json['gpu']['current_frequency'] is None:
            json['gpu']['current_frequency'] = -1
        if json['gpu']['current_temperature'] is None:
            json['gpu']['current_temperature'] = -1
        print(f"{json['gpu']['current_vram_usage']}")
        print(f"{json['gpu']['current_frequency']}")
        print(f"{json['gpu']['current_temperature']}")
        cursor.execute(
            f"""INSERT INTO `{json['id']}` (
                timestamp,
                id,
                vram,
                frequency,
                temperature
            ) 
            VALUES (
                '{json['timestamp']}',
                '{json['id']}',
                '{json['gpu']['current_vram_usage']}',
                '{json['gpu']['current_frequency']}',
                '{json['gpu']['current_temperature']}'
            );
            """
        )
        db.commit()
        cursor.close()
        db.close()

    ### DISK ###
    elif 'disk' in json:
        print(" - DISKS")
        cursor.execute( 
            "CREATE DATABASE IF NOT EXISTS disk_update;"
        )
        cursor.execute( 
            "USE disk_update;"
        )
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS `{json['id']}`(
                    timestamp VARCHAR(50),
                    id VARCHAR(50),
                    disk VARCHAR(50),
                    type VARCHAR(50),
                    capacity BIGINT,
                    used BIGINT,
                    removable VARCHAR(15)
                );
            """
        )
        for disk in json['disk']['disks']:
            print(f">> {disk}")
            cursor = db.cursor()
            if "Unknown" in json['disk']['disks'][disk]['type']:
                disk_type = "Cloud"
            else:
                disk_type = json['disk']['disks'][disk]['type']
            cursor.execute(
                f"""INSERT IGNORE INTO `{json['id']}` (
                    timestamp,
                    id,
                    disk,
                    type,
                    capacity,
                    used,
                    removable
                ) 
                VALUES (
                    '{json['timestamp']}',
                    '{json['id']}',
                    '{disk}',
                    '{disk_type}',
                    '{json['disk']['disks'][disk]['capacity']}',
                    '{json['disk']['disks'][disk]['usage']}',
                    '{str(json['disk']['disks'][disk]['is_removable'])}'
                );
                """
            )
            db.commit()
            cursor.close()
