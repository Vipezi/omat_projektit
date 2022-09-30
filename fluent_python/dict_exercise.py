#! /usr/bin/python3

#comp1 = {"name" : "comp1", "purchase" : [200, 400, 500] }



def mean_all_companies(company_list):
    result = []
    for comp in company_list:
        result.append(comp.get('mean_purchase'))
    return sum(result) / len(result)

def get_mean(purchase):
    totalsum = sum(purchase)
    amount_of_values = len(purchase)
    return totalsum / amount_of_values

    """"""
def main():
    comp1 = {"name" : "BadData", "purchase" : [200, 400, 500] }
    comp2 = {"name" : "DimDim", "purchase" : [600, 460, 234] }
    comp3 = {"name" : "MadDIM", "purchase" : [900, 760, 934] }
    company_list = [comp1, comp2, comp3]
    for comp in company_list:
        comp["mean_purchase"] = get_mean(comp["purchase"])
        print(comp)
    
    print(mean_all_companies(company_list))

if __name__ == "__main__":
    main()