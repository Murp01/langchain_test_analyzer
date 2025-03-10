import xml.etree.ElementTree as ET

def parse_junit_report(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    failures = []

    for testcase in root.findall(".//testcase"):
        failure = testcase.find("failure")
        if failure is not None:
            failures.append({
                "test": testcase.attrib["name"],
                "message": failure.attrib["message"]
            })
    
    return failures

# Test parsing
failures = parse_junit_report("test_report.xml")
print(failures)