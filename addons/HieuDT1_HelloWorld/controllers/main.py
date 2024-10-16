from odoo import _, http


class MainController(http.Controller):

    @http.route('/courses', type='http', auth="user", website=True)
    def get_courses(self):
        records = http.request.env['course.odoo'].search([])

        return http.request.render(
            "HieuDT1_HelloWorld.course_list_template",
            {"courses": records},
        )

    @http.route('/Khoa/playground', type='http', auth="user", website=True)
    def show_playground(self):
        return http.request.render(
            "HieuDT1_HelloWorld.demo_qweb",
        )

