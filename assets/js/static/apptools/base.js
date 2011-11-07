(function() {
  var AppTools, CoreAPI, CoreAgentAPI, CoreDevAPI, CoreEventsAPI, CorePushAPI, CoreRPCAPI, CoreUserAPI, RPCAPI, RPCRequest;
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; }, __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __slice = Array.prototype.slice;
  CoreAPI = (function() {
    function CoreAPI() {}
    return CoreAPI;
  })();
  CoreDevAPI = (function() {
    __extends(CoreDevAPI, CoreAPI);
    function CoreDevAPI(fcm) {
      this.verbose = __bind(this.verbose, this);
      this.error = __bind(this.error, this);
      this.eventlog = __bind(this.eventlog, this);
      this.log = __bind(this.log, this);
      this.setDebug = __bind(this.setDebug, this);      this.config = {};
      this.environment = {};
      this.performance = {};
      this.debug = {
        logging: true,
        eventlog: true,
        verbose: true
      };
    }
    CoreDevAPI.prototype.setDebug = function(debug) {
      this.debug = debug;
      return console.log("[CoreDev] Debug has been set.", this.debug);
    };
    CoreDevAPI.prototype.log = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (!(context != null)) {
        context = '{no context}';
      }
      if (this.debug.logging === true) {
        console.log.apply(console, ["[" + module + "] INFO: " + message].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.eventlog = function() {
      var context, sublabel;
      sublabel = arguments[0], context = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      if (!(context != null)) {
        context = '{no context}';
      }
      if (this.debug.eventlog === true) {
        console.log.apply(console, ["[EventLog] " + sublabel].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.error = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.logging === true) {
        console.log.apply(console, ["[" + module + "] ERROR: " + message].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.verbose = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.verbose === true) {
        this.log.apply(this, [module, message].concat(__slice.call(context)));
      }
    };
    return CoreDevAPI;
  })();
  CoreAgentAPI = (function() {
    __extends(CoreAgentAPI, CoreAPI);
    function CoreAgentAPI(fcm) {
      this._data = {};
      this.platform = {};
      this.capabilities = {};
      this._data = {
        browsers: [
          {
            string: navigator.userAgent,
            subString: "Chrome",
            identity: "Chrome"
          }, {
            string: navigator.userAgent,
            subString: "OmniWeb",
            versionSearch: "OmniWeb/",
            identity: "OmniWeb"
          }, {
            string: navigator.vendor,
            subString: "Apple",
            identity: "Safari",
            versionSearch: "Version"
          }, {
            prop: window.opera,
            identity: "Opera"
          }, {
            string: navigator.vendor,
            subString: "iCab",
            identity: "iCab"
          }, {
            string: navigator.vendor,
            subString: "KDE",
            identity: "Konqueror"
          }, {
            string: navigator.userAgent,
            subString: "Firefox",
            identity: "Firefox"
          }, {
            string: navigator.vendor,
            subString: "Camino",
            identity: "Camino"
          }, {
            string: navigator.userAgent,
            subString: "Netscape",
            identity: "Netscape"
          }, {
            string: navigator.userAgent,
            subString: "MSIE",
            identity: "Explorer",
            versionSearch: "MSIE"
          }, {
            string: navigator.userAgent,
            subString: "Gecko",
            identity: "Mozilla",
            versionSearch: "rv"
          }, {
            string: navigator.userAgent,
            subString: "Mozilla",
            identity: "Netscape",
            versionSearch: "Mozilla"
          }
        ],
        os: [
          {
            string: navigator.platform,
            subString: "Win",
            identity: "Windows"
          }, {
            string: navigator.platform,
            subString: "Mac",
            identity: "Mac"
          }, {
            string: navigator.userAgent,
            subString: "iPhone",
            identity: "iPhone/iPod"
          }, {
            string: navigator.platform,
            subString: "Linux",
            identity: "Linux"
          }
        ]
      };
    }
    CoreAgentAPI.prototype._makeMatch = function(data) {
      var prop, string, value, _i, _len, _results;
      _results = [];
      for (_i = 0, _len = data.length; _i < _len; _i++) {
        value = data[_i];
        string = value.string;
        prop = value.prop;
        this._data.versionSearchString = value.versionSearch || value.identity;
        if (string !== null) {
          if (value.string.indexOf(value.subString) !== -1) {
            return value.identity;
          }
        } else if (prop) {
          return value.identity;
        }
      }
      return _results;
    };
    CoreAgentAPI.prototype._makeVersion = function(dataString) {
      var index;
      index = dataString.indexOf(this._data.versionSearchString);
      if (index === -1) {} else {
        return parseFloat(dataString.substring(index + this._data.versionSearchString.length + 1));
      }
    };
    CoreAgentAPI.prototype.discover = function() {
      var browser, mobile, os, type, version;
      browser = this._makeMatch(this._data.browsers) || "unknown";
      version = this._makeVersion(navigator.userAgent) || this._makeVersion(navigator.appVersion) || "unknown";
      os = this._makeMatch(this._data.os) || "unknown";
      if (browser === 'iPod/iPhone' || browser === 'Android') {
        type = 'mobile';
        mobile = false;
      }
      this.platform = {
        os: os,
        type: type,
        vendor: navigator.vendor,
        product: navigator.product,
        browser: browser,
        version: version,
        flags: {
          mobile: mobile,
          webkit: $.browser.webkit,
          msie: $.browser.msie,
          opera: $.browser.opera,
          mozilla: $.browser.mozilla
        }
      };
      return this.capabilities = {
        cookies: navigator.cookieEnabled,
        ajax: $.support.ajax,
        canvas: Modernizr.canvas,
        geolocation: Modernizr.geolocation,
        svg: Modernizr.svg,
        workers: Modernizr.webworkers,
        history: Modernizr.history,
        sockets: Modernizr.websockets,
        storage: {
          local: Modernizr.localstorage,
          session: Modernizr.sessionstorage,
          websql: Modernizr.websqldatabase,
          object: Modernizr.indexeddb
        }
      };
    };
    return CoreAgentAPI;
  })();
  CoreEventsAPI = (function() {
    __extends(CoreEventsAPI, CoreAPI);
    function CoreEventsAPI(apptools) {
      ({
        registry: [],
        callchain: {},
        history: []
      });
      this.triggerEvent = function() {};
      this.registerEvent = function() {};
      this.registerHook = function() {};
    }
    return CoreEventsAPI;
  })();
  RPCAPI = (function() {
    function RPCAPI(name, base_uri, methods, config) {
      var method, _i, _len, _ref;
      this.name = name;
      this.base_uri = base_uri;
      this.methods = methods;
      this.config = config;
      if (this.methods.length > 0) {
        _ref = this.methods;
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          method = _ref[_i];
          this[method] = this._buildRPCMethod(method, base_uri, config);
        }
      }
    }
    RPCAPI.prototype._buildRPCMethod = function(method, base_uri, config) {
      var api, rpcMethod;
      api = this.name;
      rpcMethod = __bind(function(params, callbacks, async, opts) {
        if (params == null) {
          params = {};
        }
        if (callbacks == null) {
          callbacks = null;
        }
        if (async == null) {
          async = false;
        }
        if (opts == null) {
          opts = {};
        }
        return __bind(function(params, callbacks, async, opts) {
          var request;
          if (params == null) {
            params = {};
          }
          if (callbacks == null) {
            callbacks = null;
          }
          if (async == null) {
            async = false;
          }
          if (opts == null) {
            opts = {};
          }
          request = $.apptools.api.rpc.createRPCRequest({
            method: method,
            api: api,
            params: params || {},
            opts: opts || {},
            async: async || false
          });
          if (callbacks !== null) {
            return request.fulfill(callbacks);
          } else {
            return request;
          }
        }, this)(params, callbacks, async, opts);
      }, this);
      $.apptools.api.registerAPIMethod(api, method, base_uri, config);
      return rpcMethod;
    };
    return RPCAPI;
  })();
  RPCRequest = (function() {
    function RPCRequest(id, opts, agent) {
      this.params = {};
      this.action = null;
      this.method = null;
      this.api = null;
      this.base_uri = null;
      this.envelope = {
        id: null,
        opts: {},
        agent: {}
      };
      this.ajax = {
        accepts: 'application/json',
        async: false,
        cache: true,
        global: true,
        http_method: 'POST',
        crossDomain: false,
        processData: false,
        ifModified: false,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
      };
      if (id != null) {
        this.envelope.id = id;
      }
      if (opts != null) {
        this.envelope.opts = opts;
      }
      if (agent != null) {
        this.envelope.agent = agent;
      }
    }
    RPCRequest.prototype.fulfill = function() {
      var callbacks, config, defaultFailureCallback, defaultSuccessCallback;
      callbacks = arguments[0], config = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      if (!(callbacks != null ? callbacks.success : void 0)) {
        defaultSuccessCallback = __bind(function(context) {
          return $.apptools.dev.log('RPC', 'RPC succeeded but had no success callback.', this);
        }, this);
        callbacks.success = defaultSuccessCallback;
      }
      if (!(callbacks != null ? callbacks.failure : void 0)) {
        defaultFailureCallback = __bind(function(context) {
          return $.apptools.dev.error('RPC', 'RPC failed but had no failure callback.', this);
        }, this);
        callbacks.failure = defaultFailureCallback;
      }
      return $.apptools.api.rpc.fulfillRPCRequest(config, this, callbacks);
    };
    RPCRequest.prototype.setAsync = function(async) {
      var _ref, _ref2;
      if ((_ref = this.ajax) != null) {
        if ((_ref2 = _ref.async) == null) {
          _ref.async = async;
        }
      }
      return this;
    };
    RPCRequest.prototype.setOpts = function(opts) {
      var _ref, _ref2;
      if ((_ref = this.envelope) != null) {
        if ((_ref2 = _ref.opts) == null) {
          _ref.opts = opts;
        }
      }
      return this;
    };
    RPCRequest.prototype.setAgent = function(agent) {
      var _ref, _ref2;
      if ((_ref = this.envelope) != null) {
        if ((_ref2 = _ref.agent) == null) {
          _ref.agent = agent;
        }
      }
      return this;
    };
    RPCRequest.prototype.setAction = function(action) {
      this.action = action;
      return this;
    };
    RPCRequest.prototype.setMethod = function(method) {
      this.method = method;
      return this;
    };
    RPCRequest.prototype.setAPI = function(api) {
      this.api = api;
      return this;
    };
    RPCRequest.prototype.setBaseURI = function(base_uri) {
      this.base_uri = base_uri;
      return this;
    };
    RPCRequest.prototype.setParams = function(params) {
      this.params = params != null ? params : {};
      return this;
    };
    RPCRequest.prototype.payload = function() {
      var _payload;
      _payload = {
        id: this.envelope.id,
        opts: this.envelope.opts,
        agent: this.envelope.agent,
        request: {
          params: this.params,
          method: this.method,
          api: this.api
        }
      };
      return _payload;
    };
    return RPCRequest;
  })();
  CoreRPCAPI = (function() {
    __extends(CoreRPCAPI, CoreAPI);
    function CoreRPCAPI(apptools) {
      var original_xhr, _ref;
      apptools.events.registerEvent('RPC_CREATE');
      apptools.events.registerEvent('RPC_FULFILL');
      apptools.events.registerEvent('RPC_SUCCESS');
      apptools.events.registerEvent('RPC_ERROR');
      apptools.events.registerEvent('RPC_COMPLETE');
      apptools.events.registerEvent('RPC_PROGRESS');
      if (window.amplify != null) {
        apptools.dev.verbose('RPC', 'AmplifyJS detected. Registering.');
        if (apptools != null ? (_ref = apptools.sys) != null ? _ref.drivers : void 0 : void 0) {
          apptools.sys.drivers.register('transport', 'amplify', window.amplify, true, true);
        }
      }
      this.base_rpc_uri = '/_api/rpc';
      original_xhr = $.ajaxSettings.xhr;
      this.internals = {
        transports: {
          xhr: {
            factory: __bind(function() {
              var req;
              req = original_xhr();
              if (req) {
                if (typeof req.addEventListener === 'function') {
                  req.addEventListener("progress", __bind(function(ev) {
                    return apptools.events.triggerEvent('RPC_PROGRESS', {
                      event: ev
                    });
                  }, this), false);
                }
              }
              return req;
            }, this)
          }
        }
      };
      $.ajaxSetup({
        global: true,
        xhr: __bind(function() {
          return this.internals.transports.xhr.factory();
        }, this)
      });
      this.rpc = {
        lastRequest: null,
        lastFailure: null,
        lastResponse: null,
        action_prefix: null,
        history: {},
        used_ids: [],
        factory: function(name, base_uri, methods, config) {
          return $.apptools.api[name] = new RPCAPI(name, base_uri, methods, config);
        },
        _assembleRPCURL: function(method, api, prefix, base_uri) {
          if (api == null) {
            api = null;
          }
          if (prefix == null) {
            prefix = null;
          }
          if (base_uri == null) {
            base_uri = null;
          }
          if (api === null && base_uri === null) {
            throw "[RPC] Error: Must specify either an API or base URI to generate an RPC endpoint.";
          } else {
            if (base_uri === null) {
              base_uri = $.apptools.api.base_rpc_uri + '/' + api;
            }
            if (prefix !== null) {
              return [prefix + base_uri, method].join('.');
            } else {
              return [base_uri, method].join('.');
            }
          }
        },
        provisionRequestID: function() {
          var id;
          if (this.used_ids.length > 0) {
            id = Math.max.apply(this, this.used_ids) + 1;
            this.used_ids.push(id);
            return id;
          } else {
            this.used_ids.push(1);
            return 1;
          }
        },
        decodeRPCResponse: function(data, status, xhr, success, error) {
          return success(data, status);
        },
        createRPCRequest: function(config) {
          var request;
          request = new RPCRequest(this.provisionRequestID());
          if (config.api != null) {
            request.setAPI(config.api);
          }
          if (config.method != null) {
            request.setMethod(config.method);
          }
          if (config.agent != null) {
            request.setAgent(config.agent);
          }
          if (config.opts != null) {
            request.setOpts(config.opts);
          }
          if (config.base_uri != null) {
            request.setBaseURI(config.base_uri);
          }
          if (config.params != null) {
            request.setParams(config.params);
          }
          if (config.async != null) {
            request.setAsync(config.async);
          }
          $.apptools.dev.log('RPC', 'New Request', request, config);
          request.setAction(this._assembleRPCURL(request.method, request.api, this.action_prefix, this.base_rpc_uri));
          return request;
        },
        fulfillRPCRequest: function(config, request, callbacks) {
          var context;
          $.apptools.dev.log('RPC', 'Fulfill', config, request, callbacks);
          this.lastRequest = request;
          this.history[request.envelope.id] = {
            request: request,
            config: config,
            callbacks: callbacks
          };
          if (request.action === null) {
            if (request.method === null) {
              throw "[RPC] Error: Request must specify at least an action or method.";
            }
            if (request.base_uri === null) {
              if (request.api === null) {
                throw "[RPC] Error: Request must have an API or explicity BASE_URI.";
              } else {
                request.action = this._assembleRPCURL(request.method, request.api, this.action_prefix);
              }
            } else {
              request.action = this._assembleRPCURL(request.method, null, this.action_prefix, request.base_uri);
            }
          }
          if (request.action === null || request.action === void 0) {
            throw '[RPC] Error: Could not determine RPC action.';
          }
          context = {
            config: config,
            request: request,
            callbacks: callbacks
          };
          $.apptools.events.triggerEvent('RPC_FULFILL', context);
          (function(request, callbacks) {
            var amplify, xhr, xhr_action, xhr_settings, _ref2, _ref3;
            apptools = window.apptools;
            xhr_settings = {
              resourceId: request.api + '.' + request.method,
              url: request.action,
              data: JSON.stringify(request.payload()),
              async: request.ajax.async,
              global: request.ajax.global,
              type: request.ajax.http_method,
              accepts: request.ajax.accepts,
              crossDomain: request.ajax.crossDomain,
              dataType: request.ajax.dataType,
              processData: false,
              ifModified: request.ajax.ifModified,
              contentType: request.ajax.contentType,
              beforeSend: __bind(function(xhr, settings) {
                $.apptools.api.rpc.history[request.envelope.id].xhr = xhr;
                if (callbacks != null) {
                  if (typeof callbacks.status === "function") {
                    callbacks.status('beforeSend');
                  }
                }
                return xhr;
              }, this),
              error: __bind(function(xhr, status, error) {
                if (callbacks != null) {
                  if (typeof callbacks.status === "function") {
                    callbacks.status('error');
                  }
                }
                $.apptools.dev.error('RPC', 'Error: ', {
                  error: error,
                  status: status,
                  xhr: xhr
                });
                $.apptools.api.rpc.lastFailure = error;
                $.apptools.api.rpc.history[request.envelope.id].xhr = xhr;
                $.apptools.api.rpc.history[request.envelope.id].status = status;
                $.apptools.api.rpc.history[request.envelope.id].failure = error;
                context = {
                  xhr: xhr,
                  status: status,
                  error: error
                };
                $.apptools.events.triggerEvent('RPC_ERROR', context);
                $.apptools.events.triggerEvent('RPC_COMPLETE', context);
                return callbacks != null ? typeof callbacks.failure === "function" ? callbacks.failure(error) : void 0 : void 0;
              }, this),
              success: __bind(function(data, status, xhr) {
                if (data.status === 'ok') {
                  if (callbacks != null) {
                    if (typeof callbacks.status === "function") {
                      callbacks.status('success');
                    }
                  }
                  $.apptools.dev.log('RPC', 'Success', data, status, xhr);
                  $.apptools.api.rpc.lastResponse = data;
                  $.apptools.api.rpc.history[request.envelope.id].xhr = xhr;
                  $.apptools.api.rpc.history[request.envelope.id].status = status;
                  $.apptools.api.rpc.history[request.envelope.id].response = data;
                  context = {
                    xhr: xhr,
                    status: status,
                    data: data
                  };
                  $.apptools.events.triggerEvent('RPC_SUCCESS', context);
                  $.apptools.events.triggerEvent('RPC_COMPLETE', context);
                  $.apptools.dev.verbose('RPC', 'Success callback', callbacks);
                  return callbacks != null ? typeof callbacks.success === "function" ? callbacks.success(data.response.content, data.response.type, data) : void 0 : void 0;
                } else if (data.status === 'failure') {
                  if (callbacks != null) {
                    if (typeof callbacks.status === "function") {
                      callbacks.status('error');
                    }
                  }
                  $.apptools.dev.error('RPC', 'Error: ', {
                    error: error,
                    status: status,
                    xhr: xhr
                  });
                  $.apptools.api.rpc.lastFailure = error;
                  $.apptools.api.rpc.history[request.envelope.id].xhr = xhr;
                  $.apptools.api.rpc.history[request.envelope.id].status = status;
                  $.apptools.api.rpc.history[request.envelope.id].failure = error;
                  context = {
                    xhr: xhr,
                    status: status,
                    error: error
                  };
                  $.apptools.events.triggerEvent('RPC_ERROR', context);
                  $.apptools.events.triggerEvent('RPC_COMPLETE', context);
                  return callbacks != null ? typeof callbacks.failure === "function" ? callbacks.failure(error) : void 0 : void 0;
                }
              }, this),
              statusCode: {
                404: function() {
                  $.apptools.dev.error('RPC', 'HTTP/404', 'Could not resolve RPC action URI.');
                  return $.apptools.events.triggerEvent('RPC_ERROR', {
                    message: 'RPC 404: Could not resolve RPC action URI.',
                    code: 404
                  });
                },
                403: function() {
                  $.apptools.dev.error('RPC', 'HTTP/403', 'Not authorized to access the specified endpoint.');
                  return $.apptools.events.triggerEvent('RPC_ERROR', {
                    message: 'RPC 403: Not authorized to access the specified endpoint.',
                    code: 403
                  });
                },
                500: function() {
                  $.apptools.dev.error('RPC', 'HTTP/500', 'Internal server error.');
                  return $.apptools.events.triggerEvent('RPC_ERROR', {
                    message: 'RPC 500: Woops! Something went wrong. Please try again.',
                    code: 500
                  });
                }
              }
            };
            if ((_ref2 = $.apptools) != null ? (_ref3 = _ref2.sys) != null ? _ref3.drivers : void 0 : void 0) {
              amplify = $.apptools.sys.drivers.resolve('transport', 'amplify');
              if ((amplify != null) && amplify === !false) {
                $.apptools.dev.verbose('RPC', 'Fulfilling with AmplifyJS adapter.');
                xhr_action = amplify.request;
                xhr = xhr_action(xhr_settings);
              } else {
                $.apptools.dev.verbose('RPC', 'Fulfilling with AJAX adapter.', xhr_settings);
                xhr = $.ajax(xhr_settings.url, xhr_settings);
              }
            } else {
              $.apptools.dev.verbose('RPC', 'Fulfilling with AJAX adapter.', xhr_settings);
              xhr = $.ajax(xhr_settings.url, xhr_settings);
            }
            return $.apptools.dev.verbose('RPC', 'Resulting XHR: ', xhr);
          })(request, callbacks);
          return {
            id: request.envelope.id,
            request: request
          };
        }
      };
      this.ext = null;
      this.registerAPIMethod = function(api, name, base_uri, config) {
        var amplify, base_settings, resourceId, _ref2, _ref3;
        if ((_ref2 = $.apptools) != null ? (_ref3 = _ref2.sys) != null ? _ref3.drivers : void 0 : void 0) {
          amplify = $.apptools.sys.drivers.resolve('transport', 'amplify');
          if (amplify !== false) {
            $.apptools.dev.log('RPCAPI', 'Registering request procedure "' + api + '.' + name + '" with AmplifyJS.');
            resourceId = api + '.' + name;
            base_settings = {
              accepts: 'application/json'
            };
            ({
              type: 'POST',
              dataType: 'json',
              contentType: 'application/json',
              url: this.api._assembleRPCURL(name, api, null, base_uri),
              decoder: this.api.decodeRPCResponse
            });
            if (config.caching != null) {
              if (config.caching === true) {
                base_settings.caching = 'persist';
              }
              return amplify.request.define(resourceId, "ajax", base_settings);
            } else {
              return amplify.request.define(resourceId, "ajax", base_settings);
            }
          }
        }
      };
    }
    return CoreRPCAPI;
  })();
  window.RPCAPI = RPCAPI;
  window.RPCRequest = RPCRequest;
  CoreUserAPI = (function() {
    __extends(CoreUserAPI, CoreAPI);
    function CoreUserAPI(apptools) {}
    CoreUserAPI.prototype.setUserInfo = function() {
      return console.log('USERINFO: ', arguments);
    };
    return CoreUserAPI;
  })();
  CorePushAPI = (function() {
    __extends(CorePushAPI, CoreAPI);
    function CorePushAPI() {
      CorePushAPI.__super__.constructor.apply(this, arguments);
    }
    return CorePushAPI;
  })();
  AppTools = (function() {
    function AppTools(config) {
      this.config = config;
      this.dev = new CoreDevAPI(this);
      this.agent = new CoreAgentAPI(this);
      this.agent.discover();
      this.events = new CoreEventsAPI(this);
      this.user = new CoreUserAPI(this);
      this.api = new CoreRPCAPI(this);
      this.push = new CorePushAPI(this);
      return this;
    }
    return AppTools;
  })();
  window.apptools = new AppTools();
  if (typeof $ !== "undefined" && $ !== null) {
    $.extend({
      apptools: window.apptools
    });
  }
}).call(this);
