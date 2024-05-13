import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)


def find_incoming_by_group_number(file_path, group_number):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('.//group'):
            number = group.find('number').text
            if number == group_number:
                incoming = group.find('.//timingExbytes/incoming').text
                return incoming

        logging.info(f"No group with number {group_number} found.")
        return None
    except Exception as e:
        logging.error(f"Error occurred while parsing XML: {e}")
        return None



file_path = "groups.xml"
group_number = str(input("Введіть номер групи: "))
result = find_incoming_by_group_number(file_path, group_number)
if result:
    logging.info(f"Incoming for group {group_number}: {result}")
else:
    logging.info("No result found.")