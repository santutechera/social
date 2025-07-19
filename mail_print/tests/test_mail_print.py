# Copyright 2024 Tecnativa - Carlos Lopez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged
from odoo.tests.common import HttpCase


@tagged("post_install", "-at_install")
class TestMailPrint(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = (
            cls.env["res.partner"]
            .with_context(tracking_disable=True)
            .create({"name": "Test", "email": "test@example.com"})
        )

    def test_01_mail_print_tour(self):
        self.partner.message_post(
            body="Hello World", message_type="comment", subtype_xmlid="mail.mt_comment"
        )
        self.start_tour("/web", "mail_print.mail_print_tour", login="admin")

    def test_02_mail_note_not_print_tour(self):
        self.partner.message_post(
            body="This is a note", message_type="comment", subtype_xmlid="mail.mt_note"
        )
        self.start_tour("/web", "mail_print.mail_note_not_print_tour", login="admin")
