# Intended for PS v2.0
param(
    [string]$Path,
    [switch]$Verbose,
    [switch]$Remove,
    [switch]$RemoveQuotes
)

# $variables = Select-String -Path $Path -Pattern '^\s*[^\s=#]+=[^\s]+$' -Raw
$variables = Select-String -Path $Path -Pattern '^\s*[^\s=#]+=[^\s]+$'

foreach($var in $variables) {
    $var = $var.Line

    $keyVal = $var -split '=', 2
    $key = $keyVal[0].Trim()
    # $val = $RemoveQuotes ? $keyVal[1].Trim("'").Trim('"') : $keyVal[1]
    $val = If ($RemoveQuotes) {$keyVal[1].Trim("'").Trim('"')} Else {$keyVal[1]}
    # [Environment]::SetEnvironmentVariable($key, $Remove ? '' : $val)
    [Environment]::SetEnvironmentVariable($key, $(If ($Remove) {''} Else {$val}))
    if ($Verbose) {
        "$key=$([Environment]::GetEnvironmentVariable($key))"
    }
}