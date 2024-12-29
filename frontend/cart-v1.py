import streamlit as st
import pandas as pd
from bokeh.models import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

coffee_order = {
  "customer": "John Doe",
  "order": {
    "items": [
      {
        "Number": 1,
        "Name": "Latte",
        "Size": "Medium",
        "Quantity": 1,
        "Price": 3.50,
        "Options": {
          "Milk": 1,
          "Sugar": 1
        }
      },
      {
        "Number": 2,
        "Name": "Espresso",
        "Size": "Small",
        "Quantity": 2,
        "Price": 2.00,
        "Options": {}
      }
    ],
    "total": 7.50
  }
}

st.markdown("# Order Summary")

def order_to_markdown(order):
  items = order["order"]["items"]
  for item in items:
    options = item.pop("Options", {})
    item["Options"] = ", ".join([f"{k}: {v}" for k, v in options.items()])
  df = pd.DataFrame(items)
  return df.to_markdown(index=False)

markdown_table = order_to_markdown(coffee_order)
st.markdown(markdown_table)

def drawBtn():
    option = ...
    st.button("Find", on_click= onSearch, args= [option])
    
def onSearch(opt):
  js_code = """
  alert('Search button clicked!');
  """
  button = Button(label="Search")
  button.js_on_event("button_click", CustomJS(code=js_code))
  streamlit_bokeh_events(button, events="button_click", key="search_button")
  
drawBtn()