from example.dto.contact_dto import ContactCreateDto, ContactDetailsDto, ContactUpdateDto
from example.service.contact_service import ContactService
from flask import Blueprint
from pfms.swagger.pfms_swagger_decorator import pfms_create, pfms_details, pfms_pagination_sort_search_list, pfms_restore, pfms_delete


contact_controller = Blueprint("contact_controller", __name__, url_prefix="/api/v1/contact")
contact_service = ContactService()


@contact_controller.route("/create", methods=['POST'])
@pfms_create(request_body=ContactCreateDto)
def create():
    return contact_service.create()


@contact_controller.route("/details/<int:id>", methods=['GET'])
@pfms_details(response_obj=ContactDetailsDto)
def details(id: int):
    return contact_service.details(id)


@contact_controller.route("/update", methods=['POST'])
@pfms_create(request_body=ContactUpdateDto)
def update():
    return contact_service.update()


@contact_controller.route("/delete/<int:id>", methods=['DELETE'])
@pfms_delete()
def delete(id: int):
    return contact_service.delete(id)


@contact_controller.route("/restore/<int:id>", methods=['GET'])
@pfms_restore()
def restore(id: int):
    return contact_service.restore(id)


@contact_controller.route("/list", methods=['GET'])
@pfms_pagination_sort_search_list(response_obj=ContactDetailsDto)
def list():
    return contact_service.list()
