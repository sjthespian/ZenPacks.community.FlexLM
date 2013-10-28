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
/* ... from the example code ...
    Ext.define('Zenoss.component.FlexLMLicenseGridPanel',{
       extend: 'Zenoss.component.ComponentGridPanel',
       subComponentGridPanel: false,
*/
    ZC.FlexLMLicensePanel = Ext.extend(ZC.ComponentGridPanel, {
       constructor: function(config) {
            config = Ext.applyIf(config||{}, {
              componentType: 'FlexLMLicense',
              autoExpandColumn: 'feature',
              sortInfo: {
                    field: 'feature',
                    direction: 'ASC'
              },
              fields: [
                    {name: 'uid'},
                    {name: 'status'},
                    {name: 'severity'},
                    {name: 'usesMonitorAttribute'},
                    {name: 'vendor'},
                    {name: 'version'},
                    {name: 'feature'},
                    {name: 'port'},
                    {name: 'total'},
                    {name: 'monitor'},
                    {name: 'monitored'},
                    {name: 'locking'}
              ],
              columns: [{
                    id: 'severity',
                    dataIndex: 'severity',
                    header: _t('Events'),
                    renderer: Zenoss.render.severity,
                    sortable: true,
                    width: 50
/* Name is redundant, it's the same as the feature
              },{
                    id: 'name',
                    flex: 1,
                    dataIndex: 'name',
                    header: _t('Name')
*/
              },{
                    id: 'vendor',
                    dataIndex: 'vendor',
                    header: _t('Vendor'),
                    sortable: true,
                    width: 100
              },{
                    id: 'feature',
                    dataIndex: 'feature',
                    header: _t('Feature'),
                    sortable: true,
              },{
                    id: 'version',
                    dataIndex: 'version',
                    header: _t('Vendor'),
                    sortable: true,
                    width: 50
              },{
                    id: 'port',
                    dataIndex: 'port',
                    header: _t('Port'),
                    sortable: true,
                    width: 50
              },{
                    id: 'total',
                    dataIndex: 'total',
                    header: _t('Total Licenses'),
                    sortable: true,
                    width: 80
              },{
                    id: 'monitored',
                    dataIndex: 'monitored',
                    header: _t('Monitored'),
                    renderer: Zenoss.render.checkbox,
                    sortable: true,
                    width: 65
              },{
                    id: 'locking',
                    dataIndex: 'locking',
                    header: _t('Locking'),
                    renderer: Zenoss.render.locking_icons,
                    width: 65
              }]
            });
/* from example code */
/*            this.callParent([config]); */
            ZC.FlexLMLicensePanel.superclass.constructor.call(this, config);
       }
    });
    
    Ext.reg('FlexLMLicensePanel', ZC.FlexLMLicensePanel);
    
})();
