/** @odoo-module */

import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';

class ProjectListController extends ListController {
   setup() {
       super.setup();
   }
   _OnTestClick() {
      this.actionService.doAction({
         type: 'ir.actions.act_window',
         res_model: 'project.history.wizard',
         name:'Open Wizard',
         view_mode: 'form',
         view_type: 'form',
         views: [[false, 'form']],
         target: 'new',
         res_id: false,
      });
   }
}

registry.category("views").add("project_tree_import", {
   ...listView,
   Controller: ProjectListController,
   buttonTemplate: "button_project.ListView.Buttons",
});