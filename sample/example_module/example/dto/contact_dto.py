from example.model.contact import Contact
from marshmallow import fields
from pfms.pfapi.base.pfms_base_schema import PfDetailBaseSchema, common_exclude_append, update_exclude_append


class ContactDetailsDto(PfDetailBaseSchema):

    class Meta:
        model = Contact
        load_instance = True

    name = fields.String()
    email = fields.String()
    username = fields.String()
    password = fields.String()



class ContactCreateDto(ContactDetailsDto):
    class Meta:
        model = Contact
        load_instance = True
        exclude = common_exclude_append()


class ContactUpdateDto(ContactDetailsDto):
    class Meta:
        model = Contact
        load_instance = True
        exclude = update_exclude_append()

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"})
