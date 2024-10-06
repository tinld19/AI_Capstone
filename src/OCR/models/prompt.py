PROMT_OCR = """
data: {data}
Base on data above, just only return json format, in json include information by key, value.
Try to extract information by key or information that has a relationship or meaning similar to the key, if the key and value do not exist, set the value of that key to ""
Sample output:
   {
      Sender information: {
         Sender name: ""
         Sender address: ""
         Sender phone number: ""
         Sender email: ""
         Sender tax identification number: ""
      },

      Receiver information: {
         Receiver name: ""
         Receiver address: ""
         Receiver phone number: ""
         Receiver email: ""
         Receiver tax identification number: ""
      },

      Goods Information: {
         Contract number: ""
         Contract date: ""
         HS code: ""
         Currency: ""
         Country of Origin: ""
         Country of Import: ""
         Incoterms: ""
         Method of Transportation: ""
         Mode of Transport: ""
         Carrier Information: ""
         Bill of lading number: ""
         Bill of lading date: ""
         Invoice number: ""
         Invoice date: ""
         Total invoice value: ""
      },

      Tax and fee information: {
         Applicable tax types: ""
         Tax code: ""
         Tax rate: ""
         Tax amount: ""
         Import duty: ""
         Value added tax: ""
         Special consumption tax: ""
         Customs fees: ""
         Inspection fees: ""
         Other fees: ""
      }
   }
"""