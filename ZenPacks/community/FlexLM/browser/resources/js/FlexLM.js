/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an FlexLMDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');


/*
 * Friendly names for the components. First parameter is the meta_type in your
 * custom component class. Second parameter is the singular form of the
 * friendly name to be displayed in the UI. Third parameter is the plural form.
 */
ZC.registerName('FlexLMLicense', _t('FlexLM License'), _t('FlexLM Licenses'));


/*
 * Custom component grid panel. This controls the grid that gets displayed for
 * components of the type set in "componenType".
 */
/*Ext.define('Zenoss.component.FlexLMLicenseGridPanel',{
    extend: 'Zenoss.component.ComponentGridPanel',
    subComponentGridPanel: false,
*/
ZC.FlexLMLicenseGridPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'FlexLMLicense',
	    autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'description'},
                {name: 'total'},
                {name: 'inuse'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name')
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true,
                width: 40
            },{
                id: 'total',
                dataIndex: 'total',
                header: _t('Total'),
                sortable: true,
                width: 10
            },{
                id: 'inuse',
                dataIndex: 'inuse',
                header: _t('In-Use'),
                sortable: true,
                width: 10
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.FlexLMLicenseGridPanel.superclass.constructor.call(this, config);
        /*this.callParent([config]);*/
    }
});

Ext.reg('FlexLMLicenseGridPanel', ZC.FlexLMLicenseGridPanel);

})();
