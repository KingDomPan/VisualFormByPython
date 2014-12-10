var Base_panel = new Ext.data.Record.create([
    {name: 'config_script'},
    {name: 'import_js'},
    {name: 'panel_id'},
    {name: 'remark'},
    {name: 'title'}
]);
var Panel_toolbar = new Ext.data.Record.create([
    {name: 'is_change_chart_type'},
    {name: 'is_save'},
    {name: 'position'},
    {name: 'remark'},
    {name: 'state'},
    {name: 'toolbar_id'},
    {name: 'type'}
]);
var Panel_toolbar_cfg = new Ext.data.Record.create([
    {name: 'panel_id'},
    {name: 'sort_id'},
    {name: 'toolbar_id'}
]);
var Param_component = new Ext.data.Record.create([
    {name: 'comp_cfg'},
    {name: 'comp_ds'},
    {name: 'comp_id'},
    {name: 'default_value'},
    {name: 'get_type'},
    {name: 'label'},
    {name: 'param_comp_id'}
]);
var Sql_param_cfg = new Ext.data.Record.create([
    {name: 'comp_cfg'},
    {name: 'comp_ds'},
    {name: 'comp_id'},
    {name: 'data_type'},
    {name: 'is_multiple'},
    {name: 'param_label'},
    {name: 'param_name'},
    {name: 'param_type'},
    {name: 'sort_id'},
    {name: 'sql_column'},
    {name: 'sql_id'}
]);
var Param_component = new Ext.data.Record.create([
    {name: 'comp_cfg'},
    {name: 'comp_ds'},
    {name: 'comp_id'},
    {name: 'default_value'},
    {name: 'get_type'},
    {name: 'label'},
    {name: 'param_comp_id'}
]);
var Panel_toolbar_by_param = new Ext.data.Record.create([
    {name: 'param_comp_id'},
    {name: 'sort_id'},
    {name: 'toolbar_id'},
    {name: 'width'}
]);
var Sql_cfg = new Ext.data.Record.create([
    {name: 'cursor_index'},
    {name: 'id_col'},
    {name: 'remark'},
    {name: 'sql_column'},
    {name: 'sql_id'},
    {name: 'sql_text'},
    {name: 'sql_type'}
]);
var Get_value_cfg = new Ext.data.Record.create([
    {name: 'get_value_cfg_id'},
    {name: 'get_value_id'},
    {name: 'get_value_type'},
    {name: 'remark'}
]);
var Get_value_show_cfg = new Ext.data.Record.create([
    {name: 'column_cfg_type'},
    {name: 'config_script'},
    {name: 'dblclick'},
    {name: 'default_search'},
    {name: 'filed_search'},
    {name: 'get_value_cfg_id'},
    {name: 'hidden_columns'},
    {name: 'import_css'},
    {name: 'import_js'},
    {name: 'is_forcefit'},
    {name: 'is_page'},
    {name: 'page_size'},
    {name: 'right_menu_id'},
    {name: 'title'},
    {name: 'toolbar_menu_id'}
]);
var Get_value_cfg_field = new Ext.data.Record.create([
    {name: 'config_script'},
    {name: 'get_value_cfg_id'},
    {name: 'label'},
    {name: 'name'},
    {name: 'sort_id'},
    {name: 'width'}
]);
var Get_chart_cfg = new Ext.data.Record.create([
    {name: 'caption'},
    {name: 'chart_set'},
    {name: 'chart_type'},
    {name: 'click'},
    {name: 'content_result'},
    {name: 'format_number_scale'},
    {name: 'get_value_cfg_id'},
    {name: 'grid_lines'},
    {name: 'height'},
    {name: 'is_group'},
    {name: 'is_show_values'},
    {name: 'is_show_zero'},
    {name: 'jfreechart_config'},
    {name: 'label_rotation'},
    {name: 'legend'},
    {name: 'number_prefix'},
    {name: 'order_column'},
    {name: 'other_attrs'},
    {name: 'param_format'},
    {name: 'style'},
    {name: 'title'},
    {name: 'width'},
    {name: 'x_field'},
    {name: 'x_label'},
    {name: 'y_label'}
]);
var Chart_column_cfg = new Ext.data.Record.create([
    {name: 'col_label'},
    {name: 'col_name'},
    {name: 'get_value_cfg_id'},
    {name: 'type'}
]);
var Chart_line_cfg = new Ext.data.Record.create([
    {name: 'get_value_cfg_id'},
    {name: 'line_color'},
    {name: 'line_name'},
    {name: 'line_type'},
    {name: 'style'}
]);
var Monitor_menu = new Ext.data.Record.create([
    {name: 'default_display'},
    {name: 'monitor_id'},
    {name: 'monitor_name'},
    {name: 'monitor_parent_id'},
    {name: 'monitor_url'},
    {name: 'privilege_id'},
    {name: 'record_total_get_value_cfg'},
    {name: 'remark'},
    {name: 'right_corner_menu_id'},
    {name: 'sort_id'},
    {name: 'state'}
]);