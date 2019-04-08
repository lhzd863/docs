package main

import (
        "log"
        "net/http"

        "github.com/emicklei/go-restful"
        restfulspec "github.com/emicklei/go-restful-openapi"
        "github.com/go-openapi/spec"
        "github.com/lhzd863/oauth-2/token"
)

// JobResource is the REST layer to the User domain
type TokenResource struct {
        // normally one would use DAO (data access object)
        //mtoken map[string]TokenInfo
        //pgdb *db.Pgdb
        AccessToken string
        TokenState string
}

// WebService creates a new service that can handle REST requests for User resources.
func (tr TokenResource) WebService() *restful.WebService {
        ws := new(restful.WebService)
        ws.
                Path("/api/token").
                Consumes(restful.MIME_JSON, restful.MIME_JSON).
                Produces(restful.MIME_JSON, restful.MIME_JSON) // you can specify this per route as well

        tags := []string{"mtoken"}

        ws.Route(ws.POST("").To(tr.createToken).
                // docs
                Doc("post token string").
                Metadata(restfulspec.KeyOpenAPITags, tags).
                Writes(TokenResource{}). // on the response
                Returns(200, "OK", TokenResource{}).
                Returns(404, "Not Found", nil))

        ws.Route(ws.POST("/verify").To(tr.verifyAccessToken).
                // docs
                Doc("post verify token string").
                Metadata(restfulspec.KeyOpenAPITags, tags).
                Writes(TokenResource{}). // on the response
                Returns(200, "OK", TokenResource{}).
                Returns(404, "Not Found", nil))

        return ws
}

func (tr *TokenResource) createToken(request *restful.Request, response *restful.Response) {
        apara := new(AccessPara)
        err := request.ReadEntity(&apara)
        jwtt, _ := token.NewJWTToken()
        jwtt.Exp = apara.Exp
        jwtt.Iat = apara.Iat
        tokenString := jwtt.JWTTokenString()
        tr.AccessToken = tokenString
        if err == nil {
                response.WriteHeaderAndEntity(http.StatusCreated, tr)
        } else {
                response.WriteError(http.StatusInternalServerError, err)
        }
}

func (tr *TokenResource) verifyToken(request *restful.Request, response *restful.Response) {
        apara := new(Access_Token)
        err := request.ReadEntity(&apara)

        jwtt, _ := token.NewJWTToken()
        tokenState := jwtt.JWTTokenVerify(apara.AccessToken)
        tr.AccessToken = apara.AccessToken
        tr.TokenState = tokenState
        if err == nil {
                response.WriteHeaderAndEntity(http.StatusCreated, tr)
        } else {
                response.WriteError(http.StatusInternalServerError, err)
        }
}

func (tr *TokenResource) verifyAccessToken(request *restful.Request, response *restful.Response) {
        vars := r.URL.Query();
        accesstoken := vars["accesstoken"][0]

        jwtt, _ := token.NewJWTToken()
        tokenState := jwtt.JWTTokenVerify(accesstoken)
        tr.AccessToken = accesstoken
        tr.TokenState = tokenState
        if err == nil {
                response.WriteHeaderAndEntity(http.StatusCreated, tr)
        } else {
                response.WriteError(http.StatusInternalServerError, err)
        }
}

func main() {
        //pg ,_ := db.NewConnectDB("192.168.1.189",5432,"test","test","edw")
        tr := TokenResource{}
        restful.DefaultContainer.Add(tr.WebService())

        config := restfulspec.Config{
                WebServices:                   restful.RegisteredWebServices(), // you control what services are visible
                APIPath:                       "/apidocs.json",
                PostBuildSwaggerObjectHandler: enrichSwaggerObject}
        restful.DefaultContainer.Add(restfulspec.NewOpenAPIService(config))

        // Optionally, you can install the Swagger Service which provides a nice Web UI on your REST API
        // You need to download the Swagger HTML5 assets and change the FilePath location in the config below.
        // Open http://localhost:8080/apidocs/?url=http://localhost:8080/apidocs.json
        http.Handle("/apidocs/", http.StripPrefix("/apidocs/", http.FileServer(http.Dir("/Users/emicklei/Projects/swagger-ui/dist"))))

        log.Printf("start listening on localhost:6781")
        log.Fatal(http.ListenAndServe(":6781", nil))
}

func enrichSwaggerObject(swo *spec.Swagger) {
        swo.Info = &spec.Info{
                InfoProps: spec.InfoProps{
                        Title:       "JobService",
                        Description: "Resource for managing Jobs",
                        Contact: &spec.ContactInfo{
                                Name:  "lhzd863",
                                Email: "lhzd863@126.com",
                                URL:   "http://.com",
                        },
                        License: &spec.License{
                                Name: "MIT",
                                URL:  "http://.com",
                        },
                        Version: "1.0.0",
                },
        }
        swo.Tags = []spec.Tag{spec.Tag{TagProps: spec.TagProps{
                Name:        "token",
                Description: "Managing token"}}}
}

type AccessPara struct {
        Exp string
        Iat string
        Key string
}

type Access_Token struct {
        AccessToken string
}
