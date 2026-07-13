add_rules("mode.debug", "mode.release", "plugin.compile_commands.autoupdate", {outputdir = "build"})
set_defaultmode("debug")
set_targetdir("$(builddir)")
set_languages("c++20")

if is_plat("mingw") then
    add_ldflags("-static")
end

target("hash")
    add_files(
        "hash.cpp"
    )

target("obxrac32b64")
    add_files(
        "obxrac32b64.cpp"
    )
