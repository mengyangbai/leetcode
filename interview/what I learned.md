
# Inode

https://www.jianshu.com/p/9ef6542ced92


https://restfulapi.net/http-methods/

# Detailed rest all rest code

Now look at subset of codes that specially apply to the design of a REST APIs – in some more detail.


200 (OK)
It indicates that the REST API successfully carried out whatever action the client requested, and that no more specific code in the 2xx series is appropriate.

Unlike the 204 status code, a 200 response should include a response body.The information returned with the response is dependent on the method used in the request, for example:

GET an entity corresponding to the requested resource is sent in the response;
HEAD the entity-header fields corresponding to the requested resource are sent in the response without any message-body;
POST an entity describing or containing the result of the action;
TRACE an entity containing the request message as received by the end server.

201 (Created)
A REST API responds with the 201 status code whenever a resource is created inside a collection. There may also be times when a new resource is created as a result of some controller action, in which case 201 would also be an appropriate response.

The newly created resource can be referenced by the URI(s) returned in the entity of the response, with the most specific URI for the resource given by a Location header field.

The origin server MUST create the resource before returning the 201 status code. If the action cannot be carried out immediately, the server SHOULD respond with 202 (Accepted) response instead.


202 (Accepted)
A 202 response is typically used for actions that take a long while to process. It indicates that the request has been accepted for processing, but the processing has not been completed. The request might or might not be eventually acted upon, or even maybe disallowed when processing occurs.

Its purpose is to allow a server to accept a request for some other process (perhaps a batch-oriented process that is only run once per day) without requiring that the user agent’s connection to the server persist until the process is completed.

The entity returned with this response SHOULD include an indication of the request’s current status and either a pointer to a status monitor (job queue location) or some estimate of when the user can expect the request to be fulfilled.


204 (No Content)
The 204 status code is usually sent out in response to a PUT, POST, or DELETE request when the REST API declines to send back any status message or representation in the response message’s body.

An API may also send 204 in conjunction with a GET request to indicate that the requested resource exists, but has no state representation to include in the body.

If the client is a user agent, it SHOULD NOT change its document view from that which caused the request to be sent. This response is primarily intended to allow input for actions to take place without causing a change to the user agent’s active document view, although any new or updated metainformation SHOULD be applied to the document currently in the user agent’s active view.

The 204 response MUST NOT include a message-body and thus is always terminated by the first empty line after the header fields.


301 (Moved Permanently)
The 301 status code indicates that the REST API’s resource model has been significantly redesigned and a new permanent URI has been assigned to the client’s requested resource. The REST API should specify the new URI in the response’s Location header and all future requests should be directed to the given URI.

You will hardly use this response code in your API as you can always use the API versioning for new API while retaining the old one.


302 (Found)
The HTTP response status code 302 Found is a common way of performing URL redirection. An HTTP response with this status code will additionally provide a URL in the location header field. The user agent (e.g. a web browser) is invited by a response with this code to make a second, otherwise identical, request to the new URL specified in the location field.

Many web browsers implemented this code in a manner that violated this standard, changing the request type of the new request to GET, regardless of the type employed in the original request (e.g. POST). RFC 1945 and RFC 2068 specify that the client is not allowed to change the method on the redirected request. The status codes 303 and 307 have been added for servers that wish to make unambiguously clear which kind of reaction is expected of the client.


303 (See Other)
A 303 response indicates that a controller resource has finished its work, but instead of sending a potentially unwanted response body, it sends the client the URI of a response resource. This can be the URI of a temporary status message, or the URI to some already existing, more permanent, resource.

Generally speaking, the 303 status code allows a REST API to send a reference to a resource without forcing the client to download its state. Instead, the client may send a GET request to the value of the Location header.

The 303 response MUST NOT be cached, but the response to the second (redirected) request might be cacheable.


304 (Not Modified)
This status code is similar to 204 (“No Content”) in that the response body must be empty. The key distinction is that 204 is used when there is nothing to send in the body, whereas 304 is used when the resource has not been modified since the version specified by the request headers If-Modified-Since or If-None-Match.

In such case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.

Using this saves bandwidth and reprocessing on both the server and client, as only the header data must be sent and received in comparison to the entirety of the page being re-processed by the server, then sent again using more bandwidth of the server and client.


307 (Temporary Redirect)
A 307 response indicates that the REST API is not going to process the client’s request. Instead, the client should resubmit the request to the URI specified by the response message’s Location header. However, future requests should still use the original URI.

A REST API can use this status code to assign a temporary URI to the client’s requested resource. For example, a 307 response can be used to shift a client request over to another host.

The temporary URI SHOULD be given by the Location field in the response. Unless the request method was HEAD, the entity of the response SHOULD contain a short hypertext note with a hyperlink to the new URI(s). If the 307 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued.


400 (Bad Request)
400 is the generic client-side error status, used when no other 4xx error code is appropriate. Errors can be like malformed request syntax, invalid request message parameters, or deceptive request routing etc.

The client SHOULD NOT repeat the request without modifications.


401 (Unauthorized)
A 401 error response indicates that the client tried to operate on a protected resource without providing the proper authorization. It may have provided the wrong credentials or none at all. The response must include a WWW-Authenticate header field containing a challenge applicable to the requested resource.

The client MAY repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. If the 401 response contains the same challenge as the prior response, and the user agent has already attempted authentication at least once, then the user SHOULD be presented the entity that was given in the response, since that entity might include relevant diagnostic information.


403 (Forbidden)
A 403 error response indicates that the client’s request is formed correctly, but the REST API refuses to honor it i.e. the user does not have the necessary permissions for the resource. A 403 response is not a case of insufficient client credentials; that would be 401 (“Unauthorized”).

Authentication will not help and the request SHOULD NOT be repeated. Unlike a 401 Unauthorized response, authenticating will make no difference.


404 (Not Found)
The 404 error status code indicates that the REST API can’t map the client’s URI to a resource but may be available in the future. Subsequent requests by the client are permissible.

No indication is given of whether the condition is temporary or permanent. The 410 (Gone) status code SHOULD be used if the server knows, through some internally configurable mechanism, that an old resource is permanently unavailable and has no forwarding address. This status code is commonly used when the server does not wish to reveal exactly why the request has been refused, or when no other response is applicable.


405 (Method Not Allowed)
The API responds with a 405 error to indicate that the client tried to use an HTTP method that the resource does not allow. For instance, a read-only resource could support only GET and HEAD, while a controller resource might allow GET and POST, but not PUT or DELETE.

A 405 response must include the Allow header, which lists the HTTP methods that the resource supports. For example:

Allow: GET, POST

406 (Not Acceptable)
The 406 error response indicates that the API is not able to generate any of the client’s preferred media types, as indicated by the Accept request header. For example, a client request for data formatted as application/xml will receive a 406 response if the API is only willing to format data as application/json.

If the response could be unacceptable, a user agent SHOULD temporarily stop receipt of more data and query the user for a decision on further actions.


411 Length Required	The Content-Length header was not specified.
412 Precondition Failed	Precondition failed.

429 Too Many Requests	Too many request for rate limiting.
412 (Precondition Failed)
The 412 error response indicates that the client specified one or more preconditions in its request headers, effectively telling the REST API to carry out its request only if certain conditions were met. A 412 response indicates that those conditions were not met, so instead of carrying out the request, the API sends this status code.


415 (Unsupported Media Type)
The 415 error response indicates that the API is not able to process the client’s supplied media type, as indicated by the Content-Type request header. For example, a client request including data formatted as application/xml will receive a 415 response if the API is only willing to process data formatted as application/json.

For example, the client uploads an image as image/svg+xml, but the server requires that images use a different format.


500 (Internal Server Error)
500 is the generic REST API error response. Most web frameworks automatically respond with this response status code whenever they execute some request handler code that raises an exception.

A 500 error is never the client’s fault and therefore it is reasonable for the client to retry the exact same request that triggered this response, and hope to get a different response.

API response is the generic error message, given when an unexpected condition was encountered and no more specific message is suitable.


501 (Not Implemented)
The server either does not recognize the request method, or it lacks the ability to fulfill the request. Usually, this implies future availability (e.g., a new feature of a web-service API).

500 Internal Server Error	Servers are not working as expected. The request is probably valid but needs to be requested again later.
503 Service Unavailable	Service Unavailable.

200 OK	Successful.
201 Created	Created.
400 Bad Request	Bad input parameter. Error message should indicate which one and why.
401 Unauthorized	The client passed in the invalid Auth token. Client should refresh the token and then try again.
403 Forbidden	* Customer doesn’t exist. * Application not registered. * Application try to access to properties not belong to an App. * Application try to trash/purge root node. * Application try to update contentProperties. * Operation is blocked (for third-party apps). * Customer account over quota.
404 Not Found	Resource not found.
405 Method Not Allowed	The resource doesn't support the specified HTTP verb.
409 Conflict	Conflict.

# cache rest API

# All rest API action
http://www.runoob.com/w3cnote/restful-architecture.html
https://www.ibm.com/support/knowledgecenter/en/SSZLC2_7.0.0/com.ibm.commerce.webservices.doc/concepts/cwvrest.htm
GET
POST
PUT
PATCH OPTIONS	Fetches all available REST operations	200
DELETE
OPTIONS

# DNS 深度研究
linux dns file
# aws.trainning
这个不行，还是得看回acloud guru 和whiz lab

# Devops 面试题
1.1 DevOps Hiring Principles And Guidelines
During interview, keep examining below bullet points:

Describe Status Precisely And Concisely. Talk right to the point for issues which they’re confident and pretty sure. Illustrate observations and judgments separately, thus people from other teams can easily get involved and help without confusion.
Always Ask How To Test. Yes, how to fix is important. But how to test is even more important in the long run. Without that, it would be difficult to triage problems and enforce effective monitoring.
Be A Quick Learner. If they get something wrong, that’s fine. Take a minute and explain it to them. Then ask them to apply what you’ve just said to the problem and see how their answer changes. Keep the discussion going.
Excellent Automation Mindset. Automation is one of the most important capabilities for DevOps. It dramatically helps to make the process lean and keep the whole team effective.
1.2 Basic Open Questions
1. What happens if you can’t SSH to a machine? Structured analysis talks in daily work. People should possess basic experience for sure. Further question: What if ssh is slow?
2. You get low disk warning, what to do? Explain the trouble shooting process and summarize common causes as many as possible. After resolving this issue, people should think how to avoid it happening again or auto detect it in the future. Further question: System load is high, what to do?
3. You open your website and the browsers says it’s not reachable. What do you do? This is quite a typical question, not especially for DevOps. People should have a pretty good understanding for the whole process. And how know how to verify each step properly.
4. How to write initscripts for daemon service? For “service XX start”, configure lockfile and pidfile properly. For “service XXX status”, avoid false positive by light-weight functional test like checking TCP port listening. For “service XX stop”, be prepared for service slow shutdown, instead of kill -9 brutally. Further question: Any alternative to init.d in Linux? initscript, upstart VS Systemd? What drives the change?
5. Given string of a=1, b=2, c=3, how to extract the value of b? The goal here is to look for specifics, such as first-hand scripting experience. People should be familiar popular linux toolkits like awk, sed, grep, bash, etc.
6. What’s the last code you wrote recently? Ideal candidates should be doing effective programming recently and be proud of their achievements. Culture fit and passion for tech matters. Further question: Do you have any side projects? What technical blogs or websites do you follow?
7. To hire new DevOps candidates, what questions you would ask? Totally unexpected! People who love their jobs will stand out.

1.3 Advanced Open Questions
1. Diagram the system you currently run. Do you have any criticism of the architecture you just outlined? If they really had the involvement and the responsibility they should have no problem speaking fluently about their achievements. Also know deeply for the weakness.
2. Describe the most challenging situation that you were faced with and how did you fix it? Describe the size of the environment that you automated (how many servers, small scale or large scale). What interesting issues you have encountered? You may see good candidates are shining in their eyes.
3. Ever run into break-in issues or any other security issues? Security is a big concern. You can’t easily fake it, if you have few experience. Easy Question: How do you secure a server?
4. What is the main difference between traditional CM tools like Puppet / Chef vs Ansible / SaltStack? How long have you used it for? Have you used it in production? How deeply you understand your weapons.
5. Site goes down nearly every hour on the hour. What do you look at to diagnose this?
6. How you detect manual changes in prod env?
7. Your deployment is good. Now we need to support offline deployment, what you will do? List all possible issues. And solve them one by one. They should also mention how to verify the solution. Ideally the verification should be fully automated. For example, manually disabling network to simulate offline deployment is not acceptable.
8. How does XXX work? It could be loadbalancer, nagios, chef, haproxy, or whatever. Confirm candidates are familiar with fundamental concepts. If you can’t explain it simply, you don’t understand it well enough.

