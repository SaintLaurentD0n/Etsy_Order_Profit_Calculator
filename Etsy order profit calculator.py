#!/usr/bin/env python
# coding: utf-8

# In[4]:


def calculate_etsy_fees(retail_price, shipping_cost, fulfillment_cost, fulfillment_shipping, fulfillment_tax):
    # Example fee calculation logic (you'll need to adjust this based on your actual spreadsheet formulas)
    
    # Etsy fees (assumption: 5% transaction fee, 3% + $0.25 payment processing fee)
    etsy_transaction_fee = retail_price * 0.05
    etsy_payment_processing_fee = retail_price * 0.03 + 0.25
    
    # Total Etsy fees
    total_etsy_fees = etsy_transaction_fee + etsy_payment_processing_fee
    
    # Total cost
    total_cost = fulfillment_cost + fulfillment_shipping + fulfillment_tax
    
    # Total revenue
    total_revenue = retail_price + shipping_cost
    
    # Profit
    profit = total_revenue - total_cost - total_etsy_fees
    
    return {
        "Etsy Transaction Fee": etsy_transaction_fee,
        "Etsy Payment Processing Fee": etsy_payment_processing_fee,
        "Total Etsy Fees": total_etsy_fees,
        "Total Cost": total_cost,
        "Total Revenue": total_revenue,
        "Profit": profit
    }

# ENTER VALUES HERE:
retail_price = 40
shipping_cost = 5
fulfillment_cost = 12.86
fulfillment_shipping = 4.86
fulfillment_tax = 0

fees = calculate_etsy_fees(retail_price, shipping_cost, fulfillment_cost, fulfillment_shipping, fulfillment_tax)

print(fees)


# In[ ]:




