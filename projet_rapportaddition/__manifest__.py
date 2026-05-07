{
    "name": "projet_rapportaddition",
    "summary": "CEERI report",
    "description": "Module to manage project task reports",
    "author": "Qorelis",
    "category": "Project",
    "license": "LGPL-3",
    "version": "19.0.0",
    "depends": ["base", "project", "planning"],
    "data": [
    "security/ir.model.access.csv",
    "reports/task_report_action.xml",
    "reports/task_report_template.xml",
    "reports/planning_slot_report_template.xml",
    "reports/planning_slot_report_action.xml",
    "reports/decharge_report_action.xml",       
    "reports/decharge_report_template.xml",     
    "views/project_task_view.xml",
    "views/task_report_server_action.xml",
    "views/planning_slot_views.xml",
    "views/planning_menu.xml",
],
    "assets": {
        "web.assets_backend_lazy": [
            "projet_rapportaddition/static/src/views/planning_gantt_controller_inherit.js",
        ],
    },
    "icon": "projet_rapportaddition/static/description/icon.png",
}