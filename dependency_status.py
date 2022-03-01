from bs4 import BeautifulSoup
import requests
import re
from pandas import DataFrame
deps = """
Microsoft.Azure.ConfigurationManager.4.0.0
Microsoft.Azure.KeyVault.Core.3.0.3
Microsoft.Azure.Storage.Blob.11.1.0
Microsoft.Azure.Storage.Common.11.1.0
Umbraco.ModelsBuilder.8.1.0
Umbraco.ModelsBuilder.Ui.8.1.0
Umbraco.SqlServerCE.4.0.0.1
UmbracoCms.8.4.0
UmbracoCms.Core.8.4.0
UmbracoCms.Web.8.4.0
UmbracoFileSystemProviders.Azure.2.0.0-alpha5
UmbracoFileSystemProviders.Azure.Media.2.0.0-alpha5
Microsoft.Azure.ConfigurationManager.4.0.0
Microsoft.Azure.KeyVault.Core.3.0.3
Microsoft.Azure.Storage.Blob.11.1.0
Microsoft.Azure.Storage.Common.11.1.0
Umbraco.ModelsBuilder.8.1.0
Umbraco.ModelsBuilder.Ui.8.1.0
Umbraco.SqlServerCE.4.0.0.1
UmbracoCms.8.4.0
UmbracoCms.Core.8.4.0
UmbracoCms.Web.8.4.0
UmbracoFileSystemProviders.Azure.2.0.0-alpha5
UmbracoFileSystemProviders.Azure.Media.2.0.0-alpha5
"""
deps = """
ClientDependency-Mvc5.1.9.3
ClientDependency.1.9.8
CSharpTest.Net.Collections.14.906.1403.1082
Examine.1.0.1
HtmlAgilityPack.1.9.0
ImageProcessor.2.8.0
ImageProcessor.Web.4.11.0
ImageProcessor.Web.Config.2.5.0.100
ImageProcessor.Web.PostProcessor.1.5.0
KXB.Umbraco.ContentDeliveryApi.8.4.0
LightInject.5.4.0
LightInject.Annotation.1.1.0
LightInject.Mvc.2.0.0
LightInject.Web.2.0.0
LightInject.WebApi.2.0.0
Lucene.Net.3.0.3
Markdown.2.2.1
Microsoft.AspNet.Cors.5.2.7
Microsoft.AspNet.Identity.Core.2.2.2
Microsoft.AspNet.Identity.Owin.2.2.2
Microsoft.AspNet.Mvc.5.2.7
Microsoft.AspNet.Razor.3.2.7
Microsoft.AspNet.SignalR.Core.2.4.0
Microsoft.AspNet.WebApi.5.2.7
Microsoft.AspNet.WebApi.Client.5.2.7
Microsoft.AspNet.WebApi.Core.5.2.7
Microsoft.AspNet.WebApi.Cors.5.2.7
Microsoft.AspNet.WebApi.Extensions.Compression.Server.2.0.6
Microsoft.AspNet.WebApi.WebHost.5.2.7
Microsoft.AspNet.WebPages.3.2.7
Microsoft.Azure.ConfigurationManager.4.0.0
Microsoft.Azure.KeyVault.Core.3.0.3
Microsoft.Azure.Storage.Blob.11.1.0
Microsoft.Azure.Storage.Common.11.1.0
Microsoft.CodeAnalysis.Analyzers.2.6.1
Microsoft.CodeAnalysis.Common.2.10.0
Microsoft.CodeAnalysis.CSharp.2.10.0
Microsoft.CodeDom.Providers.DotNetCompilerPlatform.2.0.1
Microsoft.CSharp.4.5.0
Microsoft.Data.Edm.5.8.4
Microsoft.Data.OData.5.8.4
Microsoft.Data.Services.Client.5.8.4
Microsoft.Extensions.DependencyInjection.Abstractions.2.2.0
Microsoft.IO.RecyclableMemoryStream.1.3.0
Microsoft.Owin.4.0.1
Microsoft.Owin.Host.SystemWeb.4.0.1
Microsoft.Owin.Security.4.0.1
Microsoft.Owin.Security.Cookies.4.0.1
Microsoft.Owin.Security.OAuth.4.0.1
Microsoft.Web.Infrastructure.1.0.0.0
MiniProfiler.4.0.165
MiniProfiler.Shared.4.0.165
Newtonsoft.Json.12.0.1
NPoco.3.9.4
Owin.1.0
Semver.2.0.4
Serilog.2.8.0
Serilog.Enrichers.Process.2.0.1
Serilog.Enrichers.Thread.3.0.0
Serilog.Filters.Expressions.2.0.0
Serilog.Formatting.Compact.1.0.0
Serilog.Formatting.Compact.Reader.1.0.3
Serilog.Settings.AppSettings.2.2.2
Serilog.Sinks.Async.1.3.0
Serilog.Sinks.File.4.0.0
Serilog.Sinks.Map.1.0.0
SharpZipLib.1.1.0
Superpower.2.3.0
System.AppContext.4.3.0
System.Collections.4.3.0
System.Collections.Concurrent.4.3.0
System.Collections.Immutable.1.5.0
System.Console.4.3.0
System.Diagnostics.Debug.4.3.0
System.Diagnostics.DiagnosticSource.4.5.1
System.Diagnostics.FileVersionInfo.4.3.0
System.Diagnostics.StackTrace.4.3.0
System.Diagnostics.Tools.4.3.0
System.Dynamic.Runtime.4.3.0
System.Globalization.4.3.0
System.IO.4.3.0
System.IO.Compression.4.3.0
System.IO.FileSystem.4.3.0
System.IO.FileSystem.Primitives.4.3.0
System.Linq.4.3.0
System.Linq.Expressions.4.3.0
System.Reflection.4.3.0
System.Reflection.Metadata.1.6.0
System.Reflection.TypeExtensions.4.5.1
System.Resources.ResourceManager.4.3.0
System.Runtime.4.3.0
System.Runtime.CompilerServices.Unsafe.4.5.2
System.Runtime.Extensions.4.3.0
System.Runtime.InteropServices.4.3.0
System.Runtime.Numerics.4.3.0
System.Security.Cryptography.Algorithms.4.3.0
System.Security.Cryptography.Encoding.4.3.0
System.Security.Cryptography.Primitives.4.3.0
System.Security.Cryptography.X509Certificates.4.3.0
System.Spatial.5.8.4
System.Text.Encoding.4.3.0
System.Text.Encoding.CodePages.4.3.0
System.Text.Encoding.Extensions.4.3.0
System.Threading.4.3.0
System.Threading.Tasks.4.3.0
System.Threading.Tasks.Dataflow.4.9.0
System.Threading.Tasks.Extensions.4.5.2
System.Threading.Tasks.Parallel.4.3.0
System.Threading.Thread.4.3.0
System.ValueTuple.4.5.0
System.Xml.ReaderWriter.4.3.0
System.Xml.XDocument.4.3.0
System.Xml.XmlDocument.4.3.0
System.Xml.XPath.4.3.0
System.Xml.XPath.XDocument.4.3.0
Umbraco.ModelsBuilder.8.1.0
Umbraco.ModelsBuilder.Ui.8.1.0
Umbraco.SqlServerCE.4.0.0.1
UmbracoCms.8.4.0
UmbracoCms.Core.8.4.0
UmbracoCms.Web.8.4.0
UmbracoFileSystemProviders.Azure.2.0.0-alpha5
UmbracoFileSystemProviders.Azure.Media.2.0.0-alpha5
WebApi.Hal.2.6.0
"""
import pickle

dep_text = list(filter(lambda n: len(n)>1,deps.split('\n')))

# print(dep_text)
def get_latest(package_name):
    css_path = "html body div#skippedToContent section.container.main-container.page-list-packages div.list-packages article.package div.row div.col-sm-11 ul.package-list li span.icon-text span.text-nowrap"
    nuget_url = r"https://www.nuget.org/packages?q="
    nuget_url = nuget_url+package_name
    soup = BeautifulSoup(requests.get(nuget_url).text,"html.parser")
    res = soup.select(css_path)[0].text
    return res

def get_updates(dep_text):
    df = DataFrame(
    {
        "Package":[],
        "In Use":[],
        "Latest":[],
        "Upgradeable?":[]
    })
    for idx,i in enumerate(dep_text):
        res = re.search("^.*?(?=\d)",i)
        package_name = res.group(0) if res.group(0)[-1] != '.' else res.group(0)[:-1]
        version = i[len(package_name):] if i[len(package_name):][0] != '.' else i[len(package_name):][1:]

        latest_version = get_latest(package_name)

        if version != latest_version:
            df.loc[idx] = [package_name,version,latest_version,True]
            # print(package_name,version,latest_version,True)
        else:
            df.loc[idx] = [package_name,version,latest_version,False]
            # print(package_name,version,latest_version,False)
    return df



# df = get_updates(dep_text)
def save_pickle(df):
    with open("dependency_dataframe.pickle","wb") as handle:
        pickle.dump(df,handle,protocol=pickle.HIGHEST_PROTOCOL)
# save_pickle(df)
def load_pickle():
    with open("dependency_dataframe.pickle","wb") as handle:
        df = pickle.load(handle)
    return df

# df = load_pickle()
# print(df)

df = get_updates(dep_text)
for i in df.columns:
    print(i,sep='\t')
for i,row in df.iterrows():
    print(row["Package"],row["In Use"],row["Latest"],row["Upgradeable?"])

# for i in range(0,len(df["Package"]),30):
#     if i+30 < len(df["Package"]):
#         print(df[i:i+30])
    # print(package_name,version)
    # return res

    # if i:
    #     res = re.match("Microsoft",i).string
    #     print(res)