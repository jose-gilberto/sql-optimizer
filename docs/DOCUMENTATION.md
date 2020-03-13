
## Lexical Analysis

### Tokens

#### Keywords
```
select    SELECT    from    FROM    where    WHERE
```

#### Identifiers
```
<letter> -> [a-z, A-Z, _]
<digit> -> [0-9]
<ID> -> <letter> (<letter>|<digit>)*
```

#### Rel Operators
```
=    <    >    <=    =>    <>    like    LIKE
```

#### Logical Operators
```
AND    and    OR    or
```

#### Special Symbols
```
,    .    *
```

#### Numbers
```
<NUM> -> <digit> <digit>* [.<digit> <digit>*]?
```

#### Text | Strings
```
<STR> -> ' .* '
```

#### Date
```
<DATE> -> '<digit><digit><digit><digit>-<digit><digit>-<digit><digit>'
```