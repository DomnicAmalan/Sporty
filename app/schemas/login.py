user = {
    "display_name" : {"datatype": "str", "required": True, "type": "text", "field_name": "Name"},
    "unique_name": {"datatype": "str", "required": True, "check": True, "type": "text", "field_name": "User ID(unique)", "check": True},
    "mobile_number": {"datatype": "int", "required": True, "check": True, "type": "number", "field_name": "Mobile"},
    "email": {"datatype": "str", "required": True, "check": True, "type": "email", "validation_rule":"", "field_name": "Email"},
}