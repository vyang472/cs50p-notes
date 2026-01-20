'''def main():
    spacecraft = {"name":"Voyager 1", "distance":163}
    print(creat_report(spacecraft))

def creat_report(spacecraft):
    return f"""
    ==========REPORT=========
    
    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    -------------------------
    """

main()'''

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01
    print(creat_report(spacecraft))

def creat_report(spacecraft):
    return f"""
    ==========REPORT=========
    
    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    -------------------------
    """

main()