import subprocess
import json
import csv

def get_value(identifier):
    get_value_url = 'http://finance.google.com/finance/info?client=ig&q=' + identifier 
    value = subprocess.Popen(['curl', '-s', get_value_url], stdout=subprocess.PIPE).communicate()[0]
    j = json.loads(value[5:len(value)-2])
    return float(j['l'])

if __name__ == "__main__":
    company_list = [];
    with open('company_list.csv','rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            company_list.extend(row)
    #print company_list   
    for company in company_list:
        share_value = get_value(company)
        print company + ':' , share_value
        
