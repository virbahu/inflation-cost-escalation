import numpy as np
def escalation_model(base_cost, cost_components, inflation_rates, periods=12):
    timeline=[]
    for t in range(periods):
        adjusted=0
        for comp,share in cost_components.items():
            rate=inflation_rates.get(comp,0.03)
            adjusted+=base_cost*share*(1+rate)**(t/12)
        timeline.append({"period":t+1,"cost":round(adjusted,2),"change_pct":round((adjusted/base_cost-1)*100,2)})
    return timeline
def contract_adjustment(original_price, indices_baseline, indices_current, formula_weights):
    adjustment=0
    for component,weight in formula_weights.items():
        if component in indices_baseline and component in indices_current:
            ratio=indices_current[component]/indices_baseline[component]
            adjustment+=weight*(ratio-1)
    new_price=original_price*(1+adjustment)
    return {"original":original_price,"adjusted":round(new_price,2),"change_pct":round(adjustment*100,2)}
if __name__=="__main__":
    components={"raw_materials":0.45,"labor":0.25,"energy":0.15,"transport":0.15}
    inflation={"raw_materials":0.08,"labor":0.05,"energy":0.12,"transport":0.10}
    timeline=escalation_model(100,components,inflation)
    print(f"Month 12 cost: ${timeline[-1]['cost']} (+{timeline[-1]['change_pct']}%)")
    adj=contract_adjustment(50,{"steel":100,"labor":100,"fuel":100},{"steel":118,"labor":106,"fuel":125},{"steel":0.5,"labor":0.3,"fuel":0.2})
    print(f"Contract adjustment: ${adj['original']} → ${adj['adjusted']} ({adj['change_pct']}%)")
