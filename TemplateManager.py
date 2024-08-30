from Template import *

# Create a new template
template = Template(template_type="Invoice", template_name="Standard Invoice Template")

# Add headers with different attributes
template.add_header(name="Invoice Number", data_type="String", mandatory=True)
template.add_header(name="Customer Name", data_type="String", mandatory=True)
template.add_header(name="Total Amount", data_type="Float", mandatory=True)
template.add_header(name="Discount", data_type="Float", mandatory=False)

# Display the template
for x in template.headers:
    print(x.name)
print(template.headers)