from conans import ConanFile, CMake, tools


class OpendhtConan(ConanFile):
    name = "opendht"
    version = "1.7.4"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Opendht here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    requires = (("GnuTLS/3.5.0@gnutls/testing"),
                ("msgpack/2.1.1@msgpack/testing"))


    def source(self):
        self.run("git clone https://github.com/savoirfairelinux/opendht.git")
        self.run("cd opendht && git checkout tags/1.7.4")


    def build(self):
        print("qrva anyad")
        print(self.deps_cpp_info["msgpack"].rootpath)
        print("az")
        vars = {'PKG_CONFIG_GnuTLS_PREFIX': self.deps_cpp_info["GnuTLS"].rootpath,
                'PKG_CONFIG_msgpack_PREFIX': self.deps_cpp_info["msgpack"].rootpath,
                'PKG_CONFIG_PATH': "%s:%s" % (self.deps_cpp_info["GnuTLS"].rootpath,self.deps_cpp_info["msgpack"].rootpath)}

        with tools.environment_append(vars):
            cmake = CMake(self)
            cmake.configure(source_folder="opendht")
            cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["opendht"]

