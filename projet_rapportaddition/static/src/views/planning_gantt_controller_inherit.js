/** @odoo-module **/

import { PlanningGanttRenderer } from "@planning/views/planning_gantt/planning_gantt_renderer";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

patch(PlanningGanttRenderer.prototype, {
    async getPopoverProps(pill) {
        const popoverProps = await super.getPopoverProps(...arguments);
        let is_employee = pill.record


        if (is_employee.employee_id === false) {

            popoverProps.buttons.push({
                text: _t("Décharge"),
                class: "btn btn-sm btn-secondary",
                onClick: async () => {
                    await this.env.services.action.doAction({
                        type: "ir.actions.report",
                        report_type: "qweb-pdf",
                        report_name: "projet_rapportaddition.report_decharge_document",
                        res_model: "planning.slot",
                        res_ids: [pill.record.id],
                        context: { active_ids: [pill.record.id] },
                    });
                },
            });




        } else {


            popoverProps.buttons.push({
                text: _t("Print"),
                class: "btn btn-sm btn-secondary",
                onClick: async () => {
                    await this.env.services.action.doAction({
                        type: "ir.actions.report",
                        report_type: "qweb-pdf",
                        report_name: "projet_rapportaddition.report_planning_slot_document",
                        res_model: "planning.slot",
                        res_ids: [pill.record.id],
                        context: { active_ids: [pill.record.id] },
                    });
                },
            });



        }

        return popoverProps;
    },
});