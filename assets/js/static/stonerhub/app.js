(function () {
  var DatagridController, LiveServicesController, NewsfeedController, SocialController, StonerHub, StonerHubController, UploadController;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  StonerHubController = (function() {
    function StonerHubController() {}
    return StonerHubController;
  })();
  DatagridController = (function() {
    __extends(DatagridController, StonerHubController);
    function DatagridController(apptools, stonerhub) {
      this._cache = {
        lower: -1
      };
      this._getkey = __bind(function(data, key) {
        var item, _i, _len;
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          item = data[_i];
          if (item.name === key) {
            return item.value;
          }
        }
        return null;
      }, this);
      this.load = __bind(function(service, source, method, params, query_params, callback) {
        var need_server, request, request_end, request_length, request_start, rpc_params;
        rpc_params = {};
        need_server = false;
        request_start = this._getkey(query_params, "iDisplayStart");
        request_length = this._getkey(query_params, "iDisplayLength");
        request_end = request_start + request_length;
        rpc_params.query = {};
        rpc_params.query.limit = request_length;
        rpc_params.query.offset = request_start;
        request = $.apptools.api.rpc.createRPCRequest({
          method: method,
          api: service,
          params: rpc_params,
          async: true
        });
        $.apptools.dev.verbose('Stonerhub:Datagrid', 'Grid RPC request: ', request);
        return request.fulfill({
          success: __bind(function(response) {
            var data_item, datatables_result, field, grid_data, obj, row, _i, _j, _len, _len2, _ref, _ref2;
            grid_data = [];
            _ref = response.data;
            for (_i = 0, _len = _ref.length; _i < _len; _i++) {
              data_item = _ref[_i];
              row = [data_item.key.value];
              obj = {};
              _ref2 = response.datagrid.columns;
              for (_j = 0, _len2 = _ref2.length; _j < _len2; _j++) {
                field = _ref2[_j];
                row.push(data_item[field]);
                obj[field] = data_item[field];
              }
              grid_data.push(row);
              $.stonerhub.models.ContentItem.register(data_item.key.value, obj);
            }
            $.apptools.dev.verbose('Stonerhub:Datagrid', 'Translated data map: ', grid_data);
            response.datagrid.columns.splice(0, 0, 'key');
            datatables_result = {
              sEcho: this._getkey(query_params, 'sEcho'),
              iTotalRecords: response.resultset.results_count,
              iTotalDisplayRecords: response.resultset.returned_count,
              aaData: grid_data,
              sColumns: response.datagrid.columns.join(',')
            };
            console.log('Final result', datatables_result);
            return callback(datatables_result);
          }, this),
          failure: __bind(function(response) {
            alert('Datagrid failure. See console.');
            return $.apptools.dev.error('Stonerhub:Datagrid', 'Grid RPC error: ', response);
          }, this)
        });
      }, this);
    }
    return DatagridController;
  })();
  LiveServicesController = (function() {
    __extends(LiveServicesController, StonerHubController);
    function LiveServicesController(stonerhub) {}
    return LiveServicesController;
  })();
  SocialController = (function() {
    __extends(SocialController, StonerHubController);
    function SocialController(stonerhub) {}
    return SocialController;
  })();
  UploadController = (function() {
    __extends(UploadController, StonerHubController);
    function UploadController(stonerhub) {}
    return UploadController;
  })();
  NewsfeedController = (function() {
    __extends(NewsfeedController, StonerHubController);
    function NewsfeedController(stonerhub) {}
    return NewsfeedController;
  })();
  StonerHub = (function() {
    function StonerHub(config) {
      this.config = config;
      this.datatables = new DatagridController(this);
      this.liveservices = new LiveServicesController(this);
      this.newsfeed = new NewsfeedController(this);
      this.social = new SocialController(this);
      this.upload = new UploadController(this);
      this.models = {
        ContentItem: {
          objects: {},
          register: function(key, object) {
            return this.objects[key] = object;
          },
          get: function(key) {
            return this.objects[key];
          }
        }
      };
      return this;
    }
    return StonerHub;
  })();
  window.stonerhub = new StonerHub();
  if (typeof $ !== "undefined" && $ !== null) {
    $.extend({
      stonerhub: window.stonerhub
    });
  }
}).call(this);
