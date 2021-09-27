from example.dto.contact_dto import ContactCreateDto, ContactUpdateDto, ContactDetailsDto
from example.model.contact import Contact
from pf_sqlalchemy.crud.pfs_rest_helper_service import PfsRestHelperService


pfs_rest_helper_service = PfsRestHelperService(Contact)


class ContactService:

    def create(self):
        return pfs_rest_helper_service.rest_create(ContactCreateDto())

    def update(self):
        return pfs_rest_helper_service.rest_update(ContactUpdateDto())

    def details(self, model_id: int):
        return pfs_rest_helper_service.rest_details(model_id, ContactDetailsDto())

    def delete(self, model_id: int):
        return pfs_rest_helper_service.rest_delete(model_id)

    def restore(self, model_id: int):
        return pfs_rest_helper_service.rest_restore(model_id)

    def list(self):
        search = []
        return pfs_rest_helper_service.rest_list(ContactDetailsDto(), search=search)
