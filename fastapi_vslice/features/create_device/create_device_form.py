from typing import Optional, List

from fastapi import Request


class CreateDeviceForm:
    def __init__(self, request: Request):
        self.request = request
        self.name: Optional[str] = None
        self.address: Optional[str] = None
        self.errors: List[str] = []

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.address = form.get('address')

    def validate(self):
        if not self.name:
            self.errors.append('Name is required')
        if not self.address:
            self.errors.append('Address is required')
        if not self.errors:
            return True
        return False

