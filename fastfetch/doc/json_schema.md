# JSON config

- [1. Property `JSON config > $schema`](#schema)
- [2. Property `JSON config > logo`](#logo)
  - [2.1. Property `JSON config > logo > oneOf > item 0`](#logo_oneOf_i0)
  - [2.2. Property `JSON config > logo > oneOf > item 1`](#logo_oneOf_i1)
  - [2.3. Property `JSON config > logo > oneOf > item 2`](#logo_oneOf_i2)
    - [2.3.1. Property `JSON config > logo > oneOf > item 2 > type`](#logo_oneOf_i2_type)
    - [2.3.2. Property `JSON config > logo > oneOf > item 2 > source`](#logo_oneOf_i2_source)
    - [2.3.3. Property `JSON config > logo > oneOf > item 2 > color`](#logo_oneOf_i2_color)
      - [2.3.3.1. Property `JSON config > logo > oneOf > item 2 > color > 1`](#logo_oneOf_i2_color_1)
      - [2.3.3.2. Property `JSON config > logo > oneOf > item 2 > color > 2`](#logo_oneOf_i2_color_2)
      - [2.3.3.3. Property `JSON config > logo > oneOf > item 2 > color > 3`](#logo_oneOf_i2_color_3)
      - [2.3.3.4. Property `JSON config > logo > oneOf > item 2 > color > 4`](#logo_oneOf_i2_color_4)
      - [2.3.3.5. Property `JSON config > logo > oneOf > item 2 > color > 5`](#logo_oneOf_i2_color_5)
      - [2.3.3.6. Property `JSON config > logo > oneOf > item 2 > color > 6`](#logo_oneOf_i2_color_6)
      - [2.3.3.7. Property `JSON config > logo > oneOf > item 2 > color > 7`](#logo_oneOf_i2_color_7)
      - [2.3.3.8. Property `JSON config > logo > oneOf > item 2 > color > 8`](#logo_oneOf_i2_color_8)
      - [2.3.3.9. Property `JSON config > logo > oneOf > item 2 > color > 9`](#logo_oneOf_i2_color_9)
    - [2.3.4. Property `JSON config > logo > oneOf > item 2 > width`](#logo_oneOf_i2_width)
    - [2.3.5. Property `JSON config > logo > oneOf > item 2 > height`](#logo_oneOf_i2_height)
    - [2.3.6. Property `JSON config > logo > oneOf > item 2 > padding`](#logo_oneOf_i2_padding)
      - [2.3.6.1. Property `JSON config > logo > oneOf > item 2 > padding > top`](#logo_oneOf_i2_padding_top)
      - [2.3.6.2. Property `JSON config > logo > oneOf > item 2 > padding > left`](#logo_oneOf_i2_padding_left)
      - [2.3.6.3. Property `JSON config > logo > oneOf > item 2 > padding > right`](#logo_oneOf_i2_padding_right)
    - [2.3.7. Property `JSON config > logo > oneOf > item 2 > printRemaining`](#logo_oneOf_i2_printRemaining)
    - [2.3.8. Property `JSON config > logo > oneOf > item 2 > preserveAspectRatio`](#logo_oneOf_i2_preserveAspectRatio)
    - [2.3.9. Property `JSON config > logo > oneOf > item 2 > recache`](#logo_oneOf_i2_recache)
    - [2.3.10. Property `JSON config > logo > oneOf > item 2 > position`](#logo_oneOf_i2_position)
    - [2.3.11. Property `JSON config > logo > oneOf > item 2 > chafa`](#logo_oneOf_i2_chafa)
      - [2.3.11.1. Property `JSON config > logo > oneOf > item 2 > chafa > fgOnly`](#logo_oneOf_i2_chafa_fgOnly)
      - [2.3.11.2. Property `JSON config > logo > oneOf > item 2 > chafa > symbols`](#logo_oneOf_i2_chafa_symbols)
      - [2.3.11.3. Property `JSON config > logo > oneOf > item 2 > chafa > canvasMode`](#logo_oneOf_i2_chafa_canvasMode)
      - [2.3.11.4. Property `JSON config > logo > oneOf > item 2 > chafa > colorSpace`](#logo_oneOf_i2_chafa_colorSpace)
      - [2.3.11.5. Property `JSON config > logo > oneOf > item 2 > chafa > ditherMode`](#logo_oneOf_i2_chafa_ditherMode)
- [3. Property `JSON config > general`](#general)
  - [3.1. Property `JSON config > general > thread`](#general_thread)
  - [3.2. Property `JSON config > general > escapeBedrock`](#general_escapeBedrock)
  - [3.3. Property `JSON config > general > playerName`](#general_playerName)
  - [3.4. Property `JSON config > general > dsForceDrm`](#general_dsForceDrm)
    - [3.4.1. Property `JSON config > general > dsForceDrm > oneOf > item 0`](#general_dsForceDrm_oneOf_i0)
    - [3.4.2. Property `JSON config > general > dsForceDrm > oneOf > item 1`](#general_dsForceDrm_oneOf_i1)
    - [3.4.3. Property `JSON config > general > dsForceDrm > oneOf > item 2`](#general_dsForceDrm_oneOf_i2)
  - [3.5. Property `JSON config > general > wmiTimeout`](#general_wmiTimeout)
  - [3.6. Property `JSON config > general > processingTimeout`](#general_processingTimeout)
  - [3.7. Property `JSON config > general > preRun`](#general_preRun)
  - [3.8. Property `JSON config > general > detectVersion`](#general_detectVersion)
- [4. Property `JSON config > display`](#display)
  - [4.1. Property `JSON config > display > stat`](#display_stat)
    - [4.1.1. Property `JSON config > display > stat > oneOf > item 0`](#display_stat_oneOf_i0)
    - [4.1.2. Property `JSON config > display > stat > oneOf > item 1`](#display_stat_oneOf_i1)
  - [4.2. Property `JSON config > display > pipe`](#display_pipe)
  - [4.3. Property `JSON config > display > showErrors`](#display_showErrors)
  - [4.4. Property `JSON config > display > disableLinewrap`](#display_disableLinewrap)
  - [4.5. Property `JSON config > display > hideCursor`](#display_hideCursor)
  - [4.6. Property `JSON config > display > separator`](#display_separator)
  - [4.7. Property `JSON config > display > color`](#display_color)
    - [4.7.1. Property `JSON config > display > color > oneOf > colors`](#display_color_oneOf_i0)
    - [4.7.2. Property `JSON config > display > color > oneOf > item 1`](#display_color_oneOf_i1)
      - [4.7.2.1. Property `JSON config > display > color > oneOf > item 1 > keys`](#display_color_oneOf_i1_keys)
      - [4.7.2.2. Property `JSON config > display > color > oneOf > item 1 > title`](#display_color_oneOf_i1_title)
      - [4.7.2.3. Property `JSON config > display > color > oneOf > item 1 > output`](#display_color_oneOf_i1_output)
      - [4.7.2.4. Property `JSON config > display > color > oneOf > item 1 > separator`](#display_color_oneOf_i1_separator)
  - [4.8. Property `JSON config > display > brightColor`](#display_brightColor)
  - [4.9. Property `JSON config > display > key`](#display_key)
    - [4.9.1. Property `JSON config > display > key > width`](#display_key_width)
    - [4.9.2. Property `JSON config > display > key > type`](#display_key_type)
    - [4.9.3. Property `JSON config > display > key > paddingLeft`](#display_key_paddingLeft)
  - [4.10. Property `JSON config > display > size`](#display_size)
    - [4.10.1. Property `JSON config > display > size > binaryPrefix`](#display_size_binaryPrefix)
      - [4.10.1.1. Property `JSON config > display > size > binaryPrefix > oneOf > item 0`](#display_size_binaryPrefix_oneOf_i0)
      - [4.10.1.2. Property `JSON config > display > size > binaryPrefix > oneOf > item 1`](#display_size_binaryPrefix_oneOf_i1)
      - [4.10.1.3. Property `JSON config > display > size > binaryPrefix > oneOf > item 2`](#display_size_binaryPrefix_oneOf_i2)
    - [4.10.2. Property `JSON config > display > size > maxPrefix`](#display_size_maxPrefix)
    - [4.10.3. Property `JSON config > display > size > ndigits`](#display_size_ndigits)
  - [4.11. Property `JSON config > display > temp`](#display_temp)
    - [4.11.1. Property `JSON config > display > temp > unit`](#display_temp_unit)
    - [4.11.2. Property `JSON config > display > temp > ndigits`](#display_temp_ndigits)
    - [4.11.3. Property `JSON config > display > temp > color`](#display_temp_color)
      - [4.11.3.1. Property `JSON config > display > temp > color > green`](#display_temp_color_green)
      - [4.11.3.2. Property `JSON config > display > temp > color > yellow`](#display_temp_color_yellow)
      - [4.11.3.3. Property `JSON config > display > temp > color > red`](#display_temp_color_red)
  - [4.12. Property `JSON config > display > bar`](#display_bar)
    - [4.12.1. Property `JSON config > display > bar > charElapsed`](#display_bar_charElapsed)
    - [4.12.2. Property `JSON config > display > bar > charTotal`](#display_bar_charTotal)
    - [4.12.3. Property `JSON config > display > bar > borderLeft`](#display_bar_borderLeft)
    - [4.12.4. Property `JSON config > display > bar > borderRight`](#display_bar_borderRight)
    - [4.12.5. Property `JSON config > display > bar > width`](#display_bar_width)
  - [4.13. Property `JSON config > display > percent`](#display_percent)
    - [4.13.1. Property `JSON config > display > percent > type`](#display_percent_type)
      - [4.13.1.1. Property `JSON config > display > percent > type > oneOf > item 0`](#display_percent_type_oneOf_i0)
      - [4.13.1.2. Property `JSON config > display > percent > type > oneOf > item 1`](#display_percent_type_oneOf_i1)
        - [4.13.1.2.1. JSON config > display > percent > type > oneOf > item 1 > item 1 items](#display_percent_type_oneOf_i1_items)
    - [4.13.2. Property `JSON config > display > percent > ndigits`](#display_percent_ndigits)
    - [4.13.3. Property `JSON config > display > percent > color`](#display_percent_color)
      - [4.13.3.1. Property `JSON config > display > percent > color > green`](#display_percent_color_green)
      - [4.13.3.2. Property `JSON config > display > percent > color > yellow`](#display_percent_color_yellow)
      - [4.13.3.3. Property `JSON config > display > percent > color > red`](#display_percent_color_red)
  - [4.14. Property `JSON config > display > freq`](#display_freq)
    - [4.14.1. Property `JSON config > display > freq > ndigits`](#display_freq_ndigits)
  - [4.15. Property `JSON config > display > noBuffer`](#display_noBuffer)
  - [4.16. Property `JSON config > display > constants`](#display_constants)
    - [4.16.1. JSON config > display > constants > constants items](#display_constants_items)
- [5. Property `JSON config > modules`](#modules)
  - [5.1. JSON config > modules > modules items](#modules_items)
    - [5.1.1. Property `JSON config > modules > modules items > anyOf > item 0`](#modules_items_anyOf_i0)
    - [5.1.2. Property `JSON config > modules > modules items > anyOf > item 1`](#modules_items_anyOf_i1)
      - [5.1.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Break`](#modules_items_anyOf_i1_oneOf_i0)
        - [5.1.2.1.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Break > type`](#modules_items_anyOf_i1_oneOf_i0_type)
      - [5.1.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery`](#modules_items_anyOf_i1_oneOf_i1)
        - [5.1.2.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > type`](#modules_items_anyOf_i1_oneOf_i1_type)
        - [5.1.2.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > useSetupApi`](#modules_items_anyOf_i1_oneOf_i1_useSetupApi)
        - [5.1.2.2.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp`](#modules_items_anyOf_i1_oneOf_i1_temp)
          - [5.1.2.2.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 0`](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i0)
          - [5.1.2.2.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1`](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1)
            - [5.1.2.2.3.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > green`](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_green)
            - [5.1.2.2.3.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > yellow`](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_yellow)
        - [5.1.2.2.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent`](#modules_items_anyOf_i1_oneOf_i1_percent)
          - [5.1.2.2.4.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > green`](#modules_items_anyOf_i1_oneOf_i1_percent_green)
          - [5.1.2.2.4.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > yellow`](#modules_items_anyOf_i1_oneOf_i1_percent_yellow)
          - [5.1.2.2.4.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > type`](#modules_items_anyOf_i1_oneOf_i1_percent_type)
        - [5.1.2.2.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > key`](#modules_items_anyOf_i1_oneOf_i1_key)
        - [5.1.2.2.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyColor`](#modules_items_anyOf_i1_oneOf_i1_keyColor)
        - [5.1.2.2.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyIcon`](#modules_items_anyOf_i1_oneOf_i1_keyIcon)
        - [5.1.2.2.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyWidth`](#modules_items_anyOf_i1_oneOf_i1_keyWidth)
        - [5.1.2.2.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > outputColor`](#modules_items_anyOf_i1_oneOf_i1_outputColor)
        - [5.1.2.2.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > format`](#modules_items_anyOf_i1_oneOf_i1_format)
      - [5.1.2.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS`](#modules_items_anyOf_i1_oneOf_i2)
        - [5.1.2.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > type`](#modules_items_anyOf_i1_oneOf_i2_type)
        - [5.1.2.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > key`](#modules_items_anyOf_i1_oneOf_i2_key)
        - [5.1.2.3.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyColor`](#modules_items_anyOf_i1_oneOf_i2_keyColor)
        - [5.1.2.3.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyIcon`](#modules_items_anyOf_i1_oneOf_i2_keyIcon)
        - [5.1.2.3.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyWidth`](#modules_items_anyOf_i1_oneOf_i2_keyWidth)
        - [5.1.2.3.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > outputColor`](#modules_items_anyOf_i1_oneOf_i2_outputColor)
        - [5.1.2.3.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > format`](#modules_items_anyOf_i1_oneOf_i2_format)
      - [5.1.2.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth`](#modules_items_anyOf_i1_oneOf_i3)
        - [5.1.2.4.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > type`](#modules_items_anyOf_i1_oneOf_i3_type)
        - [5.1.2.4.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > showDisconnected`](#modules_items_anyOf_i1_oneOf_i3_showDisconnected)
        - [5.1.2.4.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > percent`](#modules_items_anyOf_i1_oneOf_i3_percent)
        - [5.1.2.4.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > key`](#modules_items_anyOf_i1_oneOf_i3_key)
        - [5.1.2.4.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyColor`](#modules_items_anyOf_i1_oneOf_i3_keyColor)
        - [5.1.2.4.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyIcon`](#modules_items_anyOf_i1_oneOf_i3_keyIcon)
        - [5.1.2.4.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyWidth`](#modules_items_anyOf_i1_oneOf_i3_keyWidth)
        - [5.1.2.4.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > outputColor`](#modules_items_anyOf_i1_oneOf_i3_outputColor)
        - [5.1.2.4.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > format`](#modules_items_anyOf_i1_oneOf_i3_format)
      - [5.1.2.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio`](#modules_items_anyOf_i1_oneOf_i4)
        - [5.1.2.5.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > type`](#modules_items_anyOf_i1_oneOf_i4_type)
        - [5.1.2.5.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > key`](#modules_items_anyOf_i1_oneOf_i4_key)
        - [5.1.2.5.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyColor`](#modules_items_anyOf_i1_oneOf_i4_keyColor)
        - [5.1.2.5.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyIcon`](#modules_items_anyOf_i1_oneOf_i4_keyIcon)
        - [5.1.2.5.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyWidth`](#modules_items_anyOf_i1_oneOf_i4_keyWidth)
        - [5.1.2.5.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > outputColor`](#modules_items_anyOf_i1_oneOf_i4_outputColor)
        - [5.1.2.5.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > format`](#modules_items_anyOf_i1_oneOf_i4_format)
      - [5.1.2.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board`](#modules_items_anyOf_i1_oneOf_i5)
        - [5.1.2.6.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > type`](#modules_items_anyOf_i1_oneOf_i5_type)
        - [5.1.2.6.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > key`](#modules_items_anyOf_i1_oneOf_i5_key)
        - [5.1.2.6.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyColor`](#modules_items_anyOf_i1_oneOf_i5_keyColor)
        - [5.1.2.6.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyIcon`](#modules_items_anyOf_i1_oneOf_i5_keyIcon)
        - [5.1.2.6.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyWidth`](#modules_items_anyOf_i1_oneOf_i5_keyWidth)
        - [5.1.2.6.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > outputColor`](#modules_items_anyOf_i1_oneOf_i5_outputColor)
        - [5.1.2.6.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > format`](#modules_items_anyOf_i1_oneOf_i5_format)
      - [5.1.2.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager`](#modules_items_anyOf_i1_oneOf_i6)
        - [5.1.2.7.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > type`](#modules_items_anyOf_i1_oneOf_i6_type)
        - [5.1.2.7.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > key`](#modules_items_anyOf_i1_oneOf_i6_key)
        - [5.1.2.7.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyColor`](#modules_items_anyOf_i1_oneOf_i6_keyColor)
        - [5.1.2.7.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyIcon`](#modules_items_anyOf_i1_oneOf_i6_keyIcon)
        - [5.1.2.7.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyWidth`](#modules_items_anyOf_i1_oneOf_i6_keyWidth)
        - [5.1.2.7.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > outputColor`](#modules_items_anyOf_i1_oneOf_i6_outputColor)
        - [5.1.2.7.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > format`](#modules_items_anyOf_i1_oneOf_i6_format)
      - [5.1.2.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness`](#modules_items_anyOf_i1_oneOf_i7)
        - [5.1.2.8.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > type`](#modules_items_anyOf_i1_oneOf_i7_type)
        - [5.1.2.8.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > percent`](#modules_items_anyOf_i1_oneOf_i7_percent)
        - [5.1.2.8.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > ddcciSleep`](#modules_items_anyOf_i1_oneOf_i7_ddcciSleep)
        - [5.1.2.8.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > compact`](#modules_items_anyOf_i1_oneOf_i7_compact)
        - [5.1.2.8.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > key`](#modules_items_anyOf_i1_oneOf_i7_key)
        - [5.1.2.8.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyColor`](#modules_items_anyOf_i1_oneOf_i7_keyColor)
        - [5.1.2.8.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyIcon`](#modules_items_anyOf_i1_oneOf_i7_keyIcon)
        - [5.1.2.8.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyWidth`](#modules_items_anyOf_i1_oneOf_i7_keyWidth)
        - [5.1.2.8.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > outputColor`](#modules_items_anyOf_i1_oneOf_i7_outputColor)
        - [5.1.2.8.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > format`](#modules_items_anyOf_i1_oneOf_i7_format)
      - [5.1.2.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS`](#modules_items_anyOf_i1_oneOf_i8)
        - [5.1.2.9.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > type`](#modules_items_anyOf_i1_oneOf_i8_type)
        - [5.1.2.9.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > percent`](#modules_items_anyOf_i1_oneOf_i8_percent)
        - [5.1.2.9.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > key`](#modules_items_anyOf_i1_oneOf_i8_key)
        - [5.1.2.9.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyColor`](#modules_items_anyOf_i1_oneOf_i8_keyColor)
        - [5.1.2.9.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyIcon`](#modules_items_anyOf_i1_oneOf_i8_keyIcon)
        - [5.1.2.9.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyWidth`](#modules_items_anyOf_i1_oneOf_i8_keyWidth)
        - [5.1.2.9.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > outputColor`](#modules_items_anyOf_i1_oneOf_i8_outputColor)
        - [5.1.2.9.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > format`](#modules_items_anyOf_i1_oneOf_i8_format)
      - [5.1.2.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera`](#modules_items_anyOf_i1_oneOf_i9)
        - [5.1.2.10.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > type`](#modules_items_anyOf_i1_oneOf_i9_type)
        - [5.1.2.10.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > key`](#modules_items_anyOf_i1_oneOf_i9_key)
        - [5.1.2.10.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyColor`](#modules_items_anyOf_i1_oneOf_i9_keyColor)
        - [5.1.2.10.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyIcon`](#modules_items_anyOf_i1_oneOf_i9_keyIcon)
        - [5.1.2.10.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyWidth`](#modules_items_anyOf_i1_oneOf_i9_keyWidth)
        - [5.1.2.10.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > outputColor`](#modules_items_anyOf_i1_oneOf_i9_outputColor)
        - [5.1.2.10.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > format`](#modules_items_anyOf_i1_oneOf_i9_format)
      - [5.1.2.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis`](#modules_items_anyOf_i1_oneOf_i10)
        - [5.1.2.11.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > type`](#modules_items_anyOf_i1_oneOf_i10_type)
        - [5.1.2.11.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > key`](#modules_items_anyOf_i1_oneOf_i10_key)
        - [5.1.2.11.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyColor`](#modules_items_anyOf_i1_oneOf_i10_keyColor)
        - [5.1.2.11.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyIcon`](#modules_items_anyOf_i1_oneOf_i10_keyIcon)
        - [5.1.2.11.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyWidth`](#modules_items_anyOf_i1_oneOf_i10_keyWidth)
        - [5.1.2.11.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > outputColor`](#modules_items_anyOf_i1_oneOf_i10_outputColor)
        - [5.1.2.11.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > format`](#modules_items_anyOf_i1_oneOf_i10_format)
      - [5.1.2.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU`](#modules_items_anyOf_i1_oneOf_i11)
        - [5.1.2.12.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > type`](#modules_items_anyOf_i1_oneOf_i11_type)
        - [5.1.2.12.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > temp`](#modules_items_anyOf_i1_oneOf_i11_temp)
        - [5.1.2.12.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > showPeCoreCount`](#modules_items_anyOf_i1_oneOf_i11_showPeCoreCount)
        - [5.1.2.12.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > key`](#modules_items_anyOf_i1_oneOf_i11_key)
        - [5.1.2.12.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyColor`](#modules_items_anyOf_i1_oneOf_i11_keyColor)
        - [5.1.2.12.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyIcon`](#modules_items_anyOf_i1_oneOf_i11_keyIcon)
        - [5.1.2.12.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyWidth`](#modules_items_anyOf_i1_oneOf_i11_keyWidth)
        - [5.1.2.12.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > outputColor`](#modules_items_anyOf_i1_oneOf_i11_outputColor)
        - [5.1.2.12.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > format`](#modules_items_anyOf_i1_oneOf_i11_format)
      - [5.1.2.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache`](#modules_items_anyOf_i1_oneOf_i12)
        - [5.1.2.13.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > type`](#modules_items_anyOf_i1_oneOf_i12_type)
        - [5.1.2.13.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > percent`](#modules_items_anyOf_i1_oneOf_i12_percent)
        - [5.1.2.13.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > key`](#modules_items_anyOf_i1_oneOf_i12_key)
        - [5.1.2.13.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyColor`](#modules_items_anyOf_i1_oneOf_i12_keyColor)
        - [5.1.2.13.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyIcon`](#modules_items_anyOf_i1_oneOf_i12_keyIcon)
        - [5.1.2.13.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyWidth`](#modules_items_anyOf_i1_oneOf_i12_keyWidth)
        - [5.1.2.13.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > outputColor`](#modules_items_anyOf_i1_oneOf_i12_outputColor)
        - [5.1.2.13.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > format`](#modules_items_anyOf_i1_oneOf_i12_format)
      - [5.1.2.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage`](#modules_items_anyOf_i1_oneOf_i13)
        - [5.1.2.14.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > type`](#modules_items_anyOf_i1_oneOf_i13_type)
        - [5.1.2.14.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > percent`](#modules_items_anyOf_i1_oneOf_i13_percent)
        - [5.1.2.14.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > separate`](#modules_items_anyOf_i1_oneOf_i13_separate)
        - [5.1.2.14.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > waitTime`](#modules_items_anyOf_i1_oneOf_i13_waitTime)
        - [5.1.2.14.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > key`](#modules_items_anyOf_i1_oneOf_i13_key)
        - [5.1.2.14.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyColor`](#modules_items_anyOf_i1_oneOf_i13_keyColor)
        - [5.1.2.14.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyIcon`](#modules_items_anyOf_i1_oneOf_i13_keyIcon)
        - [5.1.2.14.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyWidth`](#modules_items_anyOf_i1_oneOf_i13_keyWidth)
        - [5.1.2.14.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > outputColor`](#modules_items_anyOf_i1_oneOf_i13_outputColor)
        - [5.1.2.14.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > format`](#modules_items_anyOf_i1_oneOf_i13_format)
      - [5.1.2.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors`](#modules_items_anyOf_i1_oneOf_i14)
        - [5.1.2.15.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > type`](#modules_items_anyOf_i1_oneOf_i14_type)
        - [5.1.2.15.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > symbol`](#modules_items_anyOf_i1_oneOf_i14_symbol)
        - [5.1.2.15.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > paddingLeft`](#modules_items_anyOf_i1_oneOf_i14_paddingLeft)
        - [5.1.2.15.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block`](#modules_items_anyOf_i1_oneOf_i14_block)
          - [5.1.2.15.4.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > width`](#modules_items_anyOf_i1_oneOf_i14_block_width)
          - [5.1.2.15.4.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range`](#modules_items_anyOf_i1_oneOf_i14_block_range)
            - [5.1.2.15.4.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range > range items](#modules_items_anyOf_i1_oneOf_i14_block_range_items)
        - [5.1.2.15.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > key`](#modules_items_anyOf_i1_oneOf_i14_key)
        - [5.1.2.15.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > keyIcon`](#modules_items_anyOf_i1_oneOf_i14_keyIcon)
      - [5.1.2.16. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command`](#modules_items_anyOf_i1_oneOf_i15)
        - [5.1.2.16.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > type`](#modules_items_anyOf_i1_oneOf_i15_type)
        - [5.1.2.16.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > shell`](#modules_items_anyOf_i1_oneOf_i15_shell)
        - [5.1.2.16.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > param`](#modules_items_anyOf_i1_oneOf_i15_param)
        - [5.1.2.16.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > text`](#modules_items_anyOf_i1_oneOf_i15_text)
        - [5.1.2.16.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > key`](#modules_items_anyOf_i1_oneOf_i15_key)
        - [5.1.2.16.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyColor`](#modules_items_anyOf_i1_oneOf_i15_keyColor)
        - [5.1.2.16.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyIcon`](#modules_items_anyOf_i1_oneOf_i15_keyIcon)
        - [5.1.2.16.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyWidth`](#modules_items_anyOf_i1_oneOf_i15_keyWidth)
        - [5.1.2.16.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > outputColor`](#modules_items_anyOf_i1_oneOf_i15_outputColor)
        - [5.1.2.16.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > format`](#modules_items_anyOf_i1_oneOf_i15_format)
      - [5.1.2.17. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor`](#modules_items_anyOf_i1_oneOf_i16)
        - [5.1.2.17.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > type`](#modules_items_anyOf_i1_oneOf_i16_type)
        - [5.1.2.17.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > percent`](#modules_items_anyOf_i1_oneOf_i16_percent)
        - [5.1.2.17.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > key`](#modules_items_anyOf_i1_oneOf_i16_key)
        - [5.1.2.17.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyColor`](#modules_items_anyOf_i1_oneOf_i16_keyColor)
        - [5.1.2.17.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyIcon`](#modules_items_anyOf_i1_oneOf_i16_keyIcon)
        - [5.1.2.17.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyWidth`](#modules_items_anyOf_i1_oneOf_i16_keyWidth)
        - [5.1.2.17.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > outputColor`](#modules_items_anyOf_i1_oneOf_i16_outputColor)
        - [5.1.2.17.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > format`](#modules_items_anyOf_i1_oneOf_i16_format)
      - [5.1.2.18. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom`](#modules_items_anyOf_i1_oneOf_i17)
        - [5.1.2.18.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > type`](#modules_items_anyOf_i1_oneOf_i17_type)
        - [5.1.2.18.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > key`](#modules_items_anyOf_i1_oneOf_i17_key)
        - [5.1.2.18.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyColor`](#modules_items_anyOf_i1_oneOf_i17_keyColor)
        - [5.1.2.18.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyIcon`](#modules_items_anyOf_i1_oneOf_i17_keyIcon)
        - [5.1.2.18.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyWidth`](#modules_items_anyOf_i1_oneOf_i17_keyWidth)
        - [5.1.2.18.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > outputColor`](#modules_items_anyOf_i1_oneOf_i17_outputColor)
        - [5.1.2.18.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > format`](#modules_items_anyOf_i1_oneOf_i17_format)
      - [5.1.2.19. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time`](#modules_items_anyOf_i1_oneOf_i18)
        - [5.1.2.19.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > type`](#modules_items_anyOf_i1_oneOf_i18_type)
        - [5.1.2.19.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > percent`](#modules_items_anyOf_i1_oneOf_i18_percent)
        - [5.1.2.19.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > key`](#modules_items_anyOf_i1_oneOf_i18_key)
        - [5.1.2.19.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyColor`](#modules_items_anyOf_i1_oneOf_i18_keyColor)
        - [5.1.2.19.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyIcon`](#modules_items_anyOf_i1_oneOf_i18_keyIcon)
        - [5.1.2.19.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyWidth`](#modules_items_anyOf_i1_oneOf_i18_keyWidth)
        - [5.1.2.19.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > outputColor`](#modules_items_anyOf_i1_oneOf_i18_outputColor)
        - [5.1.2.19.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > format`](#modules_items_anyOf_i1_oneOf_i18_format)
      - [5.1.2.20. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display`](#modules_items_anyOf_i1_oneOf_i19)
        - [5.1.2.20.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > type`](#modules_items_anyOf_i1_oneOf_i19_type)
        - [5.1.2.20.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > compactType`](#modules_items_anyOf_i1_oneOf_i19_compactType)
        - [5.1.2.20.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > preciseRefreshRate`](#modules_items_anyOf_i1_oneOf_i19_preciseRefreshRate)
        - [5.1.2.20.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > order`](#modules_items_anyOf_i1_oneOf_i19_order)
        - [5.1.2.20.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > key`](#modules_items_anyOf_i1_oneOf_i19_key)
        - [5.1.2.20.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyColor`](#modules_items_anyOf_i1_oneOf_i19_keyColor)
        - [5.1.2.20.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyIcon`](#modules_items_anyOf_i1_oneOf_i19_keyIcon)
        - [5.1.2.20.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyWidth`](#modules_items_anyOf_i1_oneOf_i19_keyWidth)
        - [5.1.2.20.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > outputColor`](#modules_items_anyOf_i1_oneOf_i19_outputColor)
        - [5.1.2.20.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > format`](#modules_items_anyOf_i1_oneOf_i19_format)
      - [5.1.2.21. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk`](#modules_items_anyOf_i1_oneOf_i20)
        - [5.1.2.21.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > type`](#modules_items_anyOf_i1_oneOf_i20_type)
        - [5.1.2.21.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > folders`](#modules_items_anyOf_i1_oneOf_i20_folders)
        - [5.1.2.21.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showExternal`](#modules_items_anyOf_i1_oneOf_i20_showExternal)
        - [5.1.2.21.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showHidden`](#modules_items_anyOf_i1_oneOf_i20_showHidden)
        - [5.1.2.21.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showSubvolumes`](#modules_items_anyOf_i1_oneOf_i20_showSubvolumes)
        - [5.1.2.21.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showReadOnly`](#modules_items_anyOf_i1_oneOf_i20_showReadOnly)
        - [5.1.2.21.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showUnknown`](#modules_items_anyOf_i1_oneOf_i20_showUnknown)
        - [5.1.2.21.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > useAvailable`](#modules_items_anyOf_i1_oneOf_i20_useAvailable)
        - [5.1.2.21.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > percent`](#modules_items_anyOf_i1_oneOf_i20_percent)
        - [5.1.2.21.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > key`](#modules_items_anyOf_i1_oneOf_i20_key)
        - [5.1.2.21.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyColor`](#modules_items_anyOf_i1_oneOf_i20_keyColor)
        - [5.1.2.21.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyIcon`](#modules_items_anyOf_i1_oneOf_i20_keyIcon)
        - [5.1.2.21.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyWidth`](#modules_items_anyOf_i1_oneOf_i20_keyWidth)
        - [5.1.2.21.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > outputColor`](#modules_items_anyOf_i1_oneOf_i20_outputColor)
        - [5.1.2.21.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > format`](#modules_items_anyOf_i1_oneOf_i20_format)
      - [5.1.2.22. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO`](#modules_items_anyOf_i1_oneOf_i21)
        - [5.1.2.22.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > type`](#modules_items_anyOf_i1_oneOf_i21_type)
        - [5.1.2.22.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > namePrefix`](#modules_items_anyOf_i1_oneOf_i21_namePrefix)
        - [5.1.2.22.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > detectTotal`](#modules_items_anyOf_i1_oneOf_i21_detectTotal)
        - [5.1.2.22.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > waitTime`](#modules_items_anyOf_i1_oneOf_i21_waitTime)
        - [5.1.2.22.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > key`](#modules_items_anyOf_i1_oneOf_i21_key)
        - [5.1.2.22.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyColor`](#modules_items_anyOf_i1_oneOf_i21_keyColor)
        - [5.1.2.22.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyIcon`](#modules_items_anyOf_i1_oneOf_i21_keyIcon)
        - [5.1.2.22.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyWidth`](#modules_items_anyOf_i1_oneOf_i21_keyWidth)
        - [5.1.2.22.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > outputColor`](#modules_items_anyOf_i1_oneOf_i21_outputColor)
        - [5.1.2.22.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > format`](#modules_items_anyOf_i1_oneOf_i21_format)
      - [5.1.2.23. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment`](#modules_items_anyOf_i1_oneOf_i22)
        - [5.1.2.23.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > type`](#modules_items_anyOf_i1_oneOf_i22_type)
        - [5.1.2.23.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > slowVersionDetection`](#modules_items_anyOf_i1_oneOf_i22_slowVersionDetection)
        - [5.1.2.23.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > key`](#modules_items_anyOf_i1_oneOf_i22_key)
        - [5.1.2.23.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyColor`](#modules_items_anyOf_i1_oneOf_i22_keyColor)
        - [5.1.2.23.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyIcon`](#modules_items_anyOf_i1_oneOf_i22_keyIcon)
        - [5.1.2.23.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyWidth`](#modules_items_anyOf_i1_oneOf_i22_keyWidth)
        - [5.1.2.23.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > outputColor`](#modules_items_anyOf_i1_oneOf_i22_outputColor)
        - [5.1.2.23.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > format`](#modules_items_anyOf_i1_oneOf_i22_format)
      - [5.1.2.24. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS`](#modules_items_anyOf_i1_oneOf_i23)
        - [5.1.2.24.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > type`](#modules_items_anyOf_i1_oneOf_i23_type)
        - [5.1.2.24.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > showType`](#modules_items_anyOf_i1_oneOf_i23_showType)
        - [5.1.2.24.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > key`](#modules_items_anyOf_i1_oneOf_i23_key)
        - [5.1.2.24.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyColor`](#modules_items_anyOf_i1_oneOf_i23_keyColor)
        - [5.1.2.24.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyIcon`](#modules_items_anyOf_i1_oneOf_i23_keyIcon)
        - [5.1.2.24.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyWidth`](#modules_items_anyOf_i1_oneOf_i23_keyWidth)
        - [5.1.2.24.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > outputColor`](#modules_items_anyOf_i1_oneOf_i23_outputColor)
        - [5.1.2.24.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > format`](#modules_items_anyOf_i1_oneOf_i23_format)
      - [5.1.2.25. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor`](#modules_items_anyOf_i1_oneOf_i24)
        - [5.1.2.25.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > type`](#modules_items_anyOf_i1_oneOf_i24_type)
        - [5.1.2.25.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > percent`](#modules_items_anyOf_i1_oneOf_i24_percent)
        - [5.1.2.25.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > key`](#modules_items_anyOf_i1_oneOf_i24_key)
        - [5.1.2.25.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyColor`](#modules_items_anyOf_i1_oneOf_i24_keyColor)
        - [5.1.2.25.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyIcon`](#modules_items_anyOf_i1_oneOf_i24_keyIcon)
        - [5.1.2.25.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyWidth`](#modules_items_anyOf_i1_oneOf_i24_keyWidth)
        - [5.1.2.25.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > outputColor`](#modules_items_anyOf_i1_oneOf_i24_outputColor)
        - [5.1.2.25.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > format`](#modules_items_anyOf_i1_oneOf_i24_format)
      - [5.1.2.26. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font`](#modules_items_anyOf_i1_oneOf_i25)
        - [5.1.2.26.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > type`](#modules_items_anyOf_i1_oneOf_i25_type)
        - [5.1.2.26.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > percent`](#modules_items_anyOf_i1_oneOf_i25_percent)
        - [5.1.2.26.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > key`](#modules_items_anyOf_i1_oneOf_i25_key)
        - [5.1.2.26.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyColor`](#modules_items_anyOf_i1_oneOf_i25_keyColor)
        - [5.1.2.26.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyIcon`](#modules_items_anyOf_i1_oneOf_i25_keyIcon)
        - [5.1.2.26.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyWidth`](#modules_items_anyOf_i1_oneOf_i25_keyWidth)
        - [5.1.2.26.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > outputColor`](#modules_items_anyOf_i1_oneOf_i25_outputColor)
        - [5.1.2.26.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > format`](#modules_items_anyOf_i1_oneOf_i25_format)
      - [5.1.2.27. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad`](#modules_items_anyOf_i1_oneOf_i26)
        - [5.1.2.27.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > type`](#modules_items_anyOf_i1_oneOf_i26_type)
        - [5.1.2.27.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > percent`](#modules_items_anyOf_i1_oneOf_i26_percent)
        - [5.1.2.27.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > key`](#modules_items_anyOf_i1_oneOf_i26_key)
        - [5.1.2.27.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyColor`](#modules_items_anyOf_i1_oneOf_i26_keyColor)
        - [5.1.2.27.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyIcon`](#modules_items_anyOf_i1_oneOf_i26_keyIcon)
        - [5.1.2.27.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyWidth`](#modules_items_anyOf_i1_oneOf_i26_keyWidth)
        - [5.1.2.27.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > outputColor`](#modules_items_anyOf_i1_oneOf_i26_outputColor)
        - [5.1.2.27.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > format`](#modules_items_anyOf_i1_oneOf_i26_format)
      - [5.1.2.28. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU`](#modules_items_anyOf_i1_oneOf_i27)
        - [5.1.2.28.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > type`](#modules_items_anyOf_i1_oneOf_i27_type)
        - [5.1.2.28.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > temp`](#modules_items_anyOf_i1_oneOf_i27_temp)
        - [5.1.2.28.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > driverSpecific`](#modules_items_anyOf_i1_oneOf_i27_driverSpecific)
        - [5.1.2.28.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > detectionMethod`](#modules_items_anyOf_i1_oneOf_i27_detectionMethod)
        - [5.1.2.28.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > hideType`](#modules_items_anyOf_i1_oneOf_i27_hideType)
        - [5.1.2.28.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > key`](#modules_items_anyOf_i1_oneOf_i27_key)
        - [5.1.2.28.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyColor`](#modules_items_anyOf_i1_oneOf_i27_keyColor)
        - [5.1.2.28.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyIcon`](#modules_items_anyOf_i1_oneOf_i27_keyIcon)
        - [5.1.2.28.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyWidth`](#modules_items_anyOf_i1_oneOf_i27_keyWidth)
        - [5.1.2.28.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > outputColor`](#modules_items_anyOf_i1_oneOf_i27_outputColor)
        - [5.1.2.28.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > format`](#modules_items_anyOf_i1_oneOf_i27_format)
      - [5.1.2.29. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host`](#modules_items_anyOf_i1_oneOf_i28)
        - [5.1.2.29.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > type`](#modules_items_anyOf_i1_oneOf_i28_type)
        - [5.1.2.29.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > key`](#modules_items_anyOf_i1_oneOf_i28_key)
        - [5.1.2.29.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyColor`](#modules_items_anyOf_i1_oneOf_i28_keyColor)
        - [5.1.2.29.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyIcon`](#modules_items_anyOf_i1_oneOf_i28_keyIcon)
        - [5.1.2.29.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyWidth`](#modules_items_anyOf_i1_oneOf_i28_keyWidth)
        - [5.1.2.29.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > outputColor`](#modules_items_anyOf_i1_oneOf_i28_outputColor)
        - [5.1.2.29.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > format`](#modules_items_anyOf_i1_oneOf_i28_format)
      - [5.1.2.30. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons`](#modules_items_anyOf_i1_oneOf_i29)
        - [5.1.2.30.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > type`](#modules_items_anyOf_i1_oneOf_i29_type)
        - [5.1.2.30.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > key`](#modules_items_anyOf_i1_oneOf_i29_key)
        - [5.1.2.30.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyColor`](#modules_items_anyOf_i1_oneOf_i29_keyColor)
        - [5.1.2.30.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyIcon`](#modules_items_anyOf_i1_oneOf_i29_keyIcon)
        - [5.1.2.30.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyWidth`](#modules_items_anyOf_i1_oneOf_i29_keyWidth)
        - [5.1.2.30.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > outputColor`](#modules_items_anyOf_i1_oneOf_i29_outputColor)
        - [5.1.2.30.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > format`](#modules_items_anyOf_i1_oneOf_i29_format)
      - [5.1.2.31. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System`](#modules_items_anyOf_i1_oneOf_i30)
        - [5.1.2.31.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > type`](#modules_items_anyOf_i1_oneOf_i30_type)
        - [5.1.2.31.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > key`](#modules_items_anyOf_i1_oneOf_i30_key)
        - [5.1.2.31.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyColor`](#modules_items_anyOf_i1_oneOf_i30_keyColor)
        - [5.1.2.31.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyIcon`](#modules_items_anyOf_i1_oneOf_i30_keyIcon)
        - [5.1.2.31.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyWidth`](#modules_items_anyOf_i1_oneOf_i30_keyWidth)
        - [5.1.2.31.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > outputColor`](#modules_items_anyOf_i1_oneOf_i30_outputColor)
        - [5.1.2.31.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > format`](#modules_items_anyOf_i1_oneOf_i30_format)
      - [5.1.2.32. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel`](#modules_items_anyOf_i1_oneOf_i31)
        - [5.1.2.32.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > type`](#modules_items_anyOf_i1_oneOf_i31_type)
        - [5.1.2.32.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > key`](#modules_items_anyOf_i1_oneOf_i31_key)
        - [5.1.2.32.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyColor`](#modules_items_anyOf_i1_oneOf_i31_keyColor)
        - [5.1.2.32.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyIcon`](#modules_items_anyOf_i1_oneOf_i31_keyIcon)
        - [5.1.2.32.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyWidth`](#modules_items_anyOf_i1_oneOf_i31_keyWidth)
        - [5.1.2.32.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > outputColor`](#modules_items_anyOf_i1_oneOf_i31_outputColor)
        - [5.1.2.32.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > format`](#modules_items_anyOf_i1_oneOf_i31_format)
      - [5.1.2.33. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager`](#modules_items_anyOf_i1_oneOf_i32)
        - [5.1.2.33.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > type`](#modules_items_anyOf_i1_oneOf_i32_type)
        - [5.1.2.33.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > key`](#modules_items_anyOf_i1_oneOf_i32_key)
        - [5.1.2.33.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyColor`](#modules_items_anyOf_i1_oneOf_i32_keyColor)
        - [5.1.2.33.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyIcon`](#modules_items_anyOf_i1_oneOf_i32_keyIcon)
        - [5.1.2.33.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyWidth`](#modules_items_anyOf_i1_oneOf_i32_keyWidth)
        - [5.1.2.33.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > outputColor`](#modules_items_anyOf_i1_oneOf_i32_outputColor)
        - [5.1.2.33.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > format`](#modules_items_anyOf_i1_oneOf_i32_format)
      - [5.1.2.34. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP`](#modules_items_anyOf_i1_oneOf_i33)
        - [5.1.2.34.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > type`](#modules_items_anyOf_i1_oneOf_i33_type)
        - [5.1.2.34.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv4`](#modules_items_anyOf_i1_oneOf_i33_showIpv4)
        - [5.1.2.34.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv6`](#modules_items_anyOf_i1_oneOf_i33_showIpv6)
        - [5.1.2.34.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showSpeed`](#modules_items_anyOf_i1_oneOf_i33_showSpeed)
        - [5.1.2.34.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMtu`](#modules_items_anyOf_i1_oneOf_i33_showMtu)
        - [5.1.2.34.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMac`](#modules_items_anyOf_i1_oneOf_i33_showMac)
        - [5.1.2.34.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showLoop`](#modules_items_anyOf_i1_oneOf_i33_showLoop)
        - [5.1.2.34.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showPrefixLen`](#modules_items_anyOf_i1_oneOf_i33_showPrefixLen)
        - [5.1.2.34.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showAllIps`](#modules_items_anyOf_i1_oneOf_i33_showAllIps)
        - [5.1.2.34.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showFlags`](#modules_items_anyOf_i1_oneOf_i33_showFlags)
        - [5.1.2.34.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > compact`](#modules_items_anyOf_i1_oneOf_i33_compact)
        - [5.1.2.34.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > namePrefix`](#modules_items_anyOf_i1_oneOf_i33_namePrefix)
        - [5.1.2.34.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > defaultRouteOnly`](#modules_items_anyOf_i1_oneOf_i33_defaultRouteOnly)
        - [5.1.2.34.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > key`](#modules_items_anyOf_i1_oneOf_i33_key)
        - [5.1.2.34.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyColor`](#modules_items_anyOf_i1_oneOf_i33_keyColor)
        - [5.1.2.34.16. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyIcon`](#modules_items_anyOf_i1_oneOf_i33_keyIcon)
        - [5.1.2.34.17. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyWidth`](#modules_items_anyOf_i1_oneOf_i33_keyWidth)
        - [5.1.2.34.18. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > outputColor`](#modules_items_anyOf_i1_oneOf_i33_outputColor)
        - [5.1.2.34.19. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > format`](#modules_items_anyOf_i1_oneOf_i33_format)
      - [5.1.2.35. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg`](#modules_items_anyOf_i1_oneOf_i34)
        - [5.1.2.35.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > type`](#modules_items_anyOf_i1_oneOf_i34_type)
        - [5.1.2.35.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > ndigits`](#modules_items_anyOf_i1_oneOf_i34_ndigits)
        - [5.1.2.35.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > compact`](#modules_items_anyOf_i1_oneOf_i34_compact)
        - [5.1.2.35.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > percent`](#modules_items_anyOf_i1_oneOf_i34_percent)
        - [5.1.2.35.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > key`](#modules_items_anyOf_i1_oneOf_i34_key)
        - [5.1.2.35.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyColor`](#modules_items_anyOf_i1_oneOf_i34_keyColor)
        - [5.1.2.35.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyIcon`](#modules_items_anyOf_i1_oneOf_i34_keyIcon)
        - [5.1.2.35.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyWidth`](#modules_items_anyOf_i1_oneOf_i34_keyWidth)
        - [5.1.2.35.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > outputColor`](#modules_items_anyOf_i1_oneOf_i34_outputColor)
        - [5.1.2.35.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > format`](#modules_items_anyOf_i1_oneOf_i34_format)
      - [5.1.2.36. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale`](#modules_items_anyOf_i1_oneOf_i35)
        - [5.1.2.36.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > type`](#modules_items_anyOf_i1_oneOf_i35_type)
        - [5.1.2.36.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > key`](#modules_items_anyOf_i1_oneOf_i35_key)
        - [5.1.2.36.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyColor`](#modules_items_anyOf_i1_oneOf_i35_keyColor)
        - [5.1.2.36.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyIcon`](#modules_items_anyOf_i1_oneOf_i35_keyIcon)
        - [5.1.2.36.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyWidth`](#modules_items_anyOf_i1_oneOf_i35_keyWidth)
        - [5.1.2.36.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > outputColor`](#modules_items_anyOf_i1_oneOf_i35_outputColor)
        - [5.1.2.36.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > format`](#modules_items_anyOf_i1_oneOf_i35_format)
      - [5.1.2.37. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media`](#modules_items_anyOf_i1_oneOf_i36)
        - [5.1.2.37.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > type`](#modules_items_anyOf_i1_oneOf_i36_type)
        - [5.1.2.37.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > key`](#modules_items_anyOf_i1_oneOf_i36_key)
        - [5.1.2.37.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyColor`](#modules_items_anyOf_i1_oneOf_i36_keyColor)
        - [5.1.2.37.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyIcon`](#modules_items_anyOf_i1_oneOf_i36_keyIcon)
        - [5.1.2.37.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyWidth`](#modules_items_anyOf_i1_oneOf_i36_keyWidth)
        - [5.1.2.37.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > outputColor`](#modules_items_anyOf_i1_oneOf_i36_outputColor)
        - [5.1.2.37.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > format`](#modules_items_anyOf_i1_oneOf_i36_format)
      - [5.1.2.38. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory`](#modules_items_anyOf_i1_oneOf_i37)
        - [5.1.2.38.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > type`](#modules_items_anyOf_i1_oneOf_i37_type)
        - [5.1.2.38.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > percent`](#modules_items_anyOf_i1_oneOf_i37_percent)
        - [5.1.2.38.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > key`](#modules_items_anyOf_i1_oneOf_i37_key)
        - [5.1.2.38.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyColor`](#modules_items_anyOf_i1_oneOf_i37_keyColor)
        - [5.1.2.38.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyIcon`](#modules_items_anyOf_i1_oneOf_i37_keyIcon)
        - [5.1.2.38.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyWidth`](#modules_items_anyOf_i1_oneOf_i37_keyWidth)
        - [5.1.2.38.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > outputColor`](#modules_items_anyOf_i1_oneOf_i37_outputColor)
        - [5.1.2.38.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > format`](#modules_items_anyOf_i1_oneOf_i37_format)
      - [5.1.2.39. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor`](#modules_items_anyOf_i1_oneOf_i38)
        - [5.1.2.39.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > type`](#modules_items_anyOf_i1_oneOf_i38_type)
        - [5.1.2.39.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > key`](#modules_items_anyOf_i1_oneOf_i38_key)
        - [5.1.2.39.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyColor`](#modules_items_anyOf_i1_oneOf_i38_keyColor)
        - [5.1.2.39.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyIcon`](#modules_items_anyOf_i1_oneOf_i38_keyIcon)
        - [5.1.2.39.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyWidth`](#modules_items_anyOf_i1_oneOf_i38_keyWidth)
        - [5.1.2.39.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > outputColor`](#modules_items_anyOf_i1_oneOf_i38_outputColor)
        - [5.1.2.39.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > format`](#modules_items_anyOf_i1_oneOf_i38_format)
      - [5.1.2.40. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO`](#modules_items_anyOf_i1_oneOf_i39)
        - [5.1.2.40.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > type`](#modules_items_anyOf_i1_oneOf_i39_type)
        - [5.1.2.40.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > namePrefix`](#modules_items_anyOf_i1_oneOf_i39_namePrefix)
        - [5.1.2.40.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > defaultRouteOnly`](#modules_items_anyOf_i1_oneOf_i39_defaultRouteOnly)
        - [5.1.2.40.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > detectTotal`](#modules_items_anyOf_i1_oneOf_i39_detectTotal)
        - [5.1.2.40.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > waitTime`](#modules_items_anyOf_i1_oneOf_i39_waitTime)
        - [5.1.2.40.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > key`](#modules_items_anyOf_i1_oneOf_i39_key)
        - [5.1.2.40.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyColor`](#modules_items_anyOf_i1_oneOf_i39_keyColor)
        - [5.1.2.40.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyIcon`](#modules_items_anyOf_i1_oneOf_i39_keyIcon)
        - [5.1.2.40.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyWidth`](#modules_items_anyOf_i1_oneOf_i39_keyWidth)
        - [5.1.2.40.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > outputColor`](#modules_items_anyOf_i1_oneOf_i39_outputColor)
        - [5.1.2.40.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > format`](#modules_items_anyOf_i1_oneOf_i39_format)
      - [5.1.2.41. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL`](#modules_items_anyOf_i1_oneOf_i40)
        - [5.1.2.41.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > type`](#modules_items_anyOf_i1_oneOf_i40_type)
        - [5.1.2.41.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > key`](#modules_items_anyOf_i1_oneOf_i40_key)
        - [5.1.2.41.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyColor`](#modules_items_anyOf_i1_oneOf_i40_keyColor)
        - [5.1.2.41.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyIcon`](#modules_items_anyOf_i1_oneOf_i40_keyIcon)
        - [5.1.2.41.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyWidth`](#modules_items_anyOf_i1_oneOf_i40_keyWidth)
        - [5.1.2.41.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > outputColor`](#modules_items_anyOf_i1_oneOf_i40_outputColor)
        - [5.1.2.41.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > format`](#modules_items_anyOf_i1_oneOf_i40_format)
      - [5.1.2.42. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL`](#modules_items_anyOf_i1_oneOf_i41)
        - [5.1.2.42.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > type`](#modules_items_anyOf_i1_oneOf_i41_type)
        - [5.1.2.42.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > library`](#modules_items_anyOf_i1_oneOf_i41_library)
        - [5.1.2.42.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > key`](#modules_items_anyOf_i1_oneOf_i41_key)
        - [5.1.2.42.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyColor`](#modules_items_anyOf_i1_oneOf_i41_keyColor)
        - [5.1.2.42.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyIcon`](#modules_items_anyOf_i1_oneOf_i41_keyIcon)
        - [5.1.2.42.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyWidth`](#modules_items_anyOf_i1_oneOf_i41_keyWidth)
        - [5.1.2.42.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > outputColor`](#modules_items_anyOf_i1_oneOf_i41_outputColor)
        - [5.1.2.42.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > format`](#modules_items_anyOf_i1_oneOf_i41_format)
      - [5.1.2.43. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System`](#modules_items_anyOf_i1_oneOf_i42)
        - [5.1.2.43.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > type`](#modules_items_anyOf_i1_oneOf_i42_type)
        - [5.1.2.43.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > key`](#modules_items_anyOf_i1_oneOf_i42_key)
        - [5.1.2.43.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyColor`](#modules_items_anyOf_i1_oneOf_i42_keyColor)
        - [5.1.2.43.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyIcon`](#modules_items_anyOf_i1_oneOf_i42_keyIcon)
        - [5.1.2.43.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyWidth`](#modules_items_anyOf_i1_oneOf_i42_keyWidth)
        - [5.1.2.43.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > outputColor`](#modules_items_anyOf_i1_oneOf_i42_outputColor)
        - [5.1.2.43.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > format`](#modules_items_anyOf_i1_oneOf_i42_format)
      - [5.1.2.44. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages`](#modules_items_anyOf_i1_oneOf_i43)
        - [5.1.2.44.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > type`](#modules_items_anyOf_i1_oneOf_i43_type)
        - [5.1.2.44.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled`](#modules_items_anyOf_i1_oneOf_i43_disabled)
          - [5.1.2.44.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled > disabled items](#modules_items_anyOf_i1_oneOf_i43_disabled_items)
        - [5.1.2.44.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > key`](#modules_items_anyOf_i1_oneOf_i43_key)
        - [5.1.2.44.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyColor`](#modules_items_anyOf_i1_oneOf_i43_keyColor)
        - [5.1.2.44.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyIcon`](#modules_items_anyOf_i1_oneOf_i43_keyIcon)
        - [5.1.2.44.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyWidth`](#modules_items_anyOf_i1_oneOf_i43_keyWidth)
        - [5.1.2.44.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > outputColor`](#modules_items_anyOf_i1_oneOf_i43_outputColor)
        - [5.1.2.44.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > format`](#modules_items_anyOf_i1_oneOf_i43_format)
      - [5.1.2.45. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk`](#modules_items_anyOf_i1_oneOf_i44)
        - [5.1.2.45.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > type`](#modules_items_anyOf_i1_oneOf_i44_type)
        - [5.1.2.45.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > namePrefix`](#modules_items_anyOf_i1_oneOf_i44_namePrefix)
        - [5.1.2.45.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > temp`](#modules_items_anyOf_i1_oneOf_i44_temp)
        - [5.1.2.45.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > key`](#modules_items_anyOf_i1_oneOf_i44_key)
        - [5.1.2.45.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyColor`](#modules_items_anyOf_i1_oneOf_i44_keyColor)
        - [5.1.2.45.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyIcon`](#modules_items_anyOf_i1_oneOf_i44_keyIcon)
        - [5.1.2.45.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyWidth`](#modules_items_anyOf_i1_oneOf_i44_keyWidth)
        - [5.1.2.45.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > outputColor`](#modules_items_anyOf_i1_oneOf_i44_outputColor)
        - [5.1.2.45.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > format`](#modules_items_anyOf_i1_oneOf_i44_format)
      - [5.1.2.46. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory`](#modules_items_anyOf_i1_oneOf_i45)
        - [5.1.2.46.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > type`](#modules_items_anyOf_i1_oneOf_i45_type)
        - [5.1.2.46.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > key`](#modules_items_anyOf_i1_oneOf_i45_key)
        - [5.1.2.46.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyColor`](#modules_items_anyOf_i1_oneOf_i45_keyColor)
        - [5.1.2.46.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyIcon`](#modules_items_anyOf_i1_oneOf_i45_keyIcon)
        - [5.1.2.46.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyWidth`](#modules_items_anyOf_i1_oneOf_i45_keyWidth)
        - [5.1.2.46.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > outputColor`](#modules_items_anyOf_i1_oneOf_i45_outputColor)
        - [5.1.2.46.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > format`](#modules_items_anyOf_i1_oneOf_i45_format)
      - [5.1.2.47. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player`](#modules_items_anyOf_i1_oneOf_i46)
        - [5.1.2.47.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > type`](#modules_items_anyOf_i1_oneOf_i46_type)
        - [5.1.2.47.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > key`](#modules_items_anyOf_i1_oneOf_i46_key)
        - [5.1.2.47.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyColor`](#modules_items_anyOf_i1_oneOf_i46_keyColor)
        - [5.1.2.47.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyIcon`](#modules_items_anyOf_i1_oneOf_i46_keyIcon)
        - [5.1.2.47.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyWidth`](#modules_items_anyOf_i1_oneOf_i46_keyWidth)
        - [5.1.2.47.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > outputColor`](#modules_items_anyOf_i1_oneOf_i46_outputColor)
        - [5.1.2.47.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > format`](#modules_items_anyOf_i1_oneOf_i46_format)
      - [5.1.2.48. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter`](#modules_items_anyOf_i1_oneOf_i47)
        - [5.1.2.48.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > type`](#modules_items_anyOf_i1_oneOf_i47_type)
        - [5.1.2.48.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > key`](#modules_items_anyOf_i1_oneOf_i47_key)
        - [5.1.2.48.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyColor`](#modules_items_anyOf_i1_oneOf_i47_keyColor)
        - [5.1.2.48.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyIcon`](#modules_items_anyOf_i1_oneOf_i47_keyIcon)
        - [5.1.2.48.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyWidth`](#modules_items_anyOf_i1_oneOf_i47_keyWidth)
        - [5.1.2.48.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > outputColor`](#modules_items_anyOf_i1_oneOf_i47_outputColor)
        - [5.1.2.48.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > format`](#modules_items_anyOf_i1_oneOf_i47_format)
      - [5.1.2.49. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes`](#modules_items_anyOf_i1_oneOf_i48)
        - [5.1.2.49.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > type`](#modules_items_anyOf_i1_oneOf_i48_type)
        - [5.1.2.49.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > key`](#modules_items_anyOf_i1_oneOf_i48_key)
        - [5.1.2.49.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyColor`](#modules_items_anyOf_i1_oneOf_i48_keyColor)
        - [5.1.2.49.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyIcon`](#modules_items_anyOf_i1_oneOf_i48_keyIcon)
        - [5.1.2.49.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyWidth`](#modules_items_anyOf_i1_oneOf_i48_keyWidth)
        - [5.1.2.49.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > outputColor`](#modules_items_anyOf_i1_oneOf_i48_outputColor)
        - [5.1.2.49.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > format`](#modules_items_anyOf_i1_oneOf_i48_format)
      - [5.1.2.50. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP`](#modules_items_anyOf_i1_oneOf_i49)
        - [5.1.2.50.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > type`](#modules_items_anyOf_i1_oneOf_i49_type)
        - [5.1.2.50.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > url`](#modules_items_anyOf_i1_oneOf_i49_url)
        - [5.1.2.50.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > timeout`](#modules_items_anyOf_i1_oneOf_i49_timeout)
        - [5.1.2.50.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > ipv6`](#modules_items_anyOf_i1_oneOf_i49_ipv6)
        - [5.1.2.50.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > key`](#modules_items_anyOf_i1_oneOf_i49_key)
        - [5.1.2.50.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyColor`](#modules_items_anyOf_i1_oneOf_i49_keyColor)
        - [5.1.2.50.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyIcon`](#modules_items_anyOf_i1_oneOf_i49_keyIcon)
        - [5.1.2.50.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyWidth`](#modules_items_anyOf_i1_oneOf_i49_keyWidth)
        - [5.1.2.50.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > outputColor`](#modules_items_anyOf_i1_oneOf_i49_outputColor)
        - [5.1.2.50.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > format`](#modules_items_anyOf_i1_oneOf_i49_format)
      - [5.1.2.51. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator`](#modules_items_anyOf_i1_oneOf_i50)
        - [5.1.2.51.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > type`](#modules_items_anyOf_i1_oneOf_i50_type)
        - [5.1.2.51.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > string`](#modules_items_anyOf_i1_oneOf_i50_string)
        - [5.1.2.51.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > outputColor`](#modules_items_anyOf_i1_oneOf_i50_outputColor)
        - [5.1.2.51.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > length`](#modules_items_anyOf_i1_oneOf_i50_length)
      - [5.1.2.52. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell`](#modules_items_anyOf_i1_oneOf_i51)
        - [5.1.2.52.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > type`](#modules_items_anyOf_i1_oneOf_i51_type)
        - [5.1.2.52.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > key`](#modules_items_anyOf_i1_oneOf_i51_key)
        - [5.1.2.52.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyColor`](#modules_items_anyOf_i1_oneOf_i51_keyColor)
        - [5.1.2.52.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyIcon`](#modules_items_anyOf_i1_oneOf_i51_keyIcon)
        - [5.1.2.52.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyWidth`](#modules_items_anyOf_i1_oneOf_i51_keyWidth)
        - [5.1.2.52.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > outputColor`](#modules_items_anyOf_i1_oneOf_i51_outputColor)
        - [5.1.2.52.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > format`](#modules_items_anyOf_i1_oneOf_i51_format)
      - [5.1.2.53. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound`](#modules_items_anyOf_i1_oneOf_i52)
        - [5.1.2.53.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > type`](#modules_items_anyOf_i1_oneOf_i52_type)
        - [5.1.2.53.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > soundType`](#modules_items_anyOf_i1_oneOf_i52_soundType)
        - [5.1.2.53.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > percent`](#modules_items_anyOf_i1_oneOf_i52_percent)
        - [5.1.2.53.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > key`](#modules_items_anyOf_i1_oneOf_i52_key)
        - [5.1.2.53.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyColor`](#modules_items_anyOf_i1_oneOf_i52_keyColor)
        - [5.1.2.53.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyIcon`](#modules_items_anyOf_i1_oneOf_i52_keyIcon)
        - [5.1.2.53.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyWidth`](#modules_items_anyOf_i1_oneOf_i52_keyWidth)
        - [5.1.2.53.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > outputColor`](#modules_items_anyOf_i1_oneOf_i52_outputColor)
        - [5.1.2.53.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > format`](#modules_items_anyOf_i1_oneOf_i52_format)
      - [5.1.2.54. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap`](#modules_items_anyOf_i1_oneOf_i53)
        - [5.1.2.54.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > type`](#modules_items_anyOf_i1_oneOf_i53_type)
        - [5.1.2.54.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > percent`](#modules_items_anyOf_i1_oneOf_i53_percent)
        - [5.1.2.54.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > key`](#modules_items_anyOf_i1_oneOf_i53_key)
        - [5.1.2.54.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyColor`](#modules_items_anyOf_i1_oneOf_i53_keyColor)
        - [5.1.2.54.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyIcon`](#modules_items_anyOf_i1_oneOf_i53_keyIcon)
        - [5.1.2.54.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyWidth`](#modules_items_anyOf_i1_oneOf_i53_keyWidth)
        - [5.1.2.54.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > outputColor`](#modules_items_anyOf_i1_oneOf_i53_outputColor)
        - [5.1.2.54.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > format`](#modules_items_anyOf_i1_oneOf_i53_format)
      - [5.1.2.55. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal`](#modules_items_anyOf_i1_oneOf_i54)
        - [5.1.2.55.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > type`](#modules_items_anyOf_i1_oneOf_i54_type)
        - [5.1.2.55.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > key`](#modules_items_anyOf_i1_oneOf_i54_key)
        - [5.1.2.55.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyColor`](#modules_items_anyOf_i1_oneOf_i54_keyColor)
        - [5.1.2.55.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyIcon`](#modules_items_anyOf_i1_oneOf_i54_keyIcon)
        - [5.1.2.55.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyWidth`](#modules_items_anyOf_i1_oneOf_i54_keyWidth)
        - [5.1.2.55.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > outputColor`](#modules_items_anyOf_i1_oneOf_i54_outputColor)
        - [5.1.2.55.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > format`](#modules_items_anyOf_i1_oneOf_i54_format)
      - [5.1.2.56. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font`](#modules_items_anyOf_i1_oneOf_i55)
        - [5.1.2.56.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > type`](#modules_items_anyOf_i1_oneOf_i55_type)
        - [5.1.2.56.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > key`](#modules_items_anyOf_i1_oneOf_i55_key)
        - [5.1.2.56.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyColor`](#modules_items_anyOf_i1_oneOf_i55_keyColor)
        - [5.1.2.56.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyIcon`](#modules_items_anyOf_i1_oneOf_i55_keyIcon)
        - [5.1.2.56.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyWidth`](#modules_items_anyOf_i1_oneOf_i55_keyWidth)
        - [5.1.2.56.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > outputColor`](#modules_items_anyOf_i1_oneOf_i55_outputColor)
        - [5.1.2.56.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > format`](#modules_items_anyOf_i1_oneOf_i55_format)
      - [5.1.2.57. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size`](#modules_items_anyOf_i1_oneOf_i56)
        - [5.1.2.57.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > type`](#modules_items_anyOf_i1_oneOf_i56_type)
        - [5.1.2.57.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > key`](#modules_items_anyOf_i1_oneOf_i56_key)
        - [5.1.2.57.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyColor`](#modules_items_anyOf_i1_oneOf_i56_keyColor)
        - [5.1.2.57.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyIcon`](#modules_items_anyOf_i1_oneOf_i56_keyIcon)
        - [5.1.2.57.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyWidth`](#modules_items_anyOf_i1_oneOf_i56_keyWidth)
        - [5.1.2.57.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > outputColor`](#modules_items_anyOf_i1_oneOf_i56_outputColor)
        - [5.1.2.57.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > format`](#modules_items_anyOf_i1_oneOf_i56_format)
      - [5.1.2.58. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme`](#modules_items_anyOf_i1_oneOf_i57)
        - [5.1.2.58.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > type`](#modules_items_anyOf_i1_oneOf_i57_type)
        - [5.1.2.58.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > key`](#modules_items_anyOf_i1_oneOf_i57_key)
        - [5.1.2.58.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyColor`](#modules_items_anyOf_i1_oneOf_i57_keyColor)
        - [5.1.2.58.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyIcon`](#modules_items_anyOf_i1_oneOf_i57_keyIcon)
        - [5.1.2.58.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyWidth`](#modules_items_anyOf_i1_oneOf_i57_keyWidth)
        - [5.1.2.58.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > outputColor`](#modules_items_anyOf_i1_oneOf_i57_outputColor)
        - [5.1.2.58.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > format`](#modules_items_anyOf_i1_oneOf_i57_format)
      - [5.1.2.59. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme`](#modules_items_anyOf_i1_oneOf_i58)
        - [5.1.2.59.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > type`](#modules_items_anyOf_i1_oneOf_i58_type)
        - [5.1.2.59.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > key`](#modules_items_anyOf_i1_oneOf_i58_key)
        - [5.1.2.59.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyColor`](#modules_items_anyOf_i1_oneOf_i58_keyColor)
        - [5.1.2.59.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyIcon`](#modules_items_anyOf_i1_oneOf_i58_keyIcon)
        - [5.1.2.59.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyWidth`](#modules_items_anyOf_i1_oneOf_i58_keyWidth)
        - [5.1.2.59.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > outputColor`](#modules_items_anyOf_i1_oneOf_i58_outputColor)
        - [5.1.2.59.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > format`](#modules_items_anyOf_i1_oneOf_i58_format)
      - [5.1.2.60. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title`](#modules_items_anyOf_i1_oneOf_i59)
        - [5.1.2.60.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > type`](#modules_items_anyOf_i1_oneOf_i59_type)
        - [5.1.2.60.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > fqdn`](#modules_items_anyOf_i1_oneOf_i59_fqdn)
        - [5.1.2.60.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color`](#modules_items_anyOf_i1_oneOf_i59_color)
          - [5.1.2.60.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > user`](#modules_items_anyOf_i1_oneOf_i59_color_user)
          - [5.1.2.60.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > at`](#modules_items_anyOf_i1_oneOf_i59_color_at)
          - [5.1.2.60.3.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > host`](#modules_items_anyOf_i1_oneOf_i59_color_host)
        - [5.1.2.60.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > key`](#modules_items_anyOf_i1_oneOf_i59_key)
        - [5.1.2.60.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyColor`](#modules_items_anyOf_i1_oneOf_i59_keyColor)
        - [5.1.2.60.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyIcon`](#modules_items_anyOf_i1_oneOf_i59_keyIcon)
        - [5.1.2.60.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyWidth`](#modules_items_anyOf_i1_oneOf_i59_keyWidth)
        - [5.1.2.60.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > outputColor`](#modules_items_anyOf_i1_oneOf_i59_outputColor)
        - [5.1.2.60.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > format`](#modules_items_anyOf_i1_oneOf_i59_format)
      - [5.1.2.61. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM`](#modules_items_anyOf_i1_oneOf_i60)
        - [5.1.2.61.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > type`](#modules_items_anyOf_i1_oneOf_i60_type)
        - [5.1.2.61.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > key`](#modules_items_anyOf_i1_oneOf_i60_key)
        - [5.1.2.61.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyColor`](#modules_items_anyOf_i1_oneOf_i60_keyColor)
        - [5.1.2.61.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyIcon`](#modules_items_anyOf_i1_oneOf_i60_keyIcon)
        - [5.1.2.61.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyWidth`](#modules_items_anyOf_i1_oneOf_i60_keyWidth)
        - [5.1.2.61.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > outputColor`](#modules_items_anyOf_i1_oneOf_i60_outputColor)
        - [5.1.2.61.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > format`](#modules_items_anyOf_i1_oneOf_i60_format)
      - [5.1.2.62. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users`](#modules_items_anyOf_i1_oneOf_i61)
        - [5.1.2.62.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > type`](#modules_items_anyOf_i1_oneOf_i61_type)
        - [5.1.2.62.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > compact`](#modules_items_anyOf_i1_oneOf_i61_compact)
        - [5.1.2.62.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > myselfOnly`](#modules_items_anyOf_i1_oneOf_i61_myselfOnly)
        - [5.1.2.62.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > key`](#modules_items_anyOf_i1_oneOf_i61_key)
        - [5.1.2.62.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyColor`](#modules_items_anyOf_i1_oneOf_i61_keyColor)
        - [5.1.2.62.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyIcon`](#modules_items_anyOf_i1_oneOf_i61_keyIcon)
        - [5.1.2.62.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyWidth`](#modules_items_anyOf_i1_oneOf_i61_keyWidth)
        - [5.1.2.62.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > outputColor`](#modules_items_anyOf_i1_oneOf_i61_outputColor)
        - [5.1.2.62.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > format`](#modules_items_anyOf_i1_oneOf_i61_format)
      - [5.1.2.63. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime`](#modules_items_anyOf_i1_oneOf_i62)
        - [5.1.2.63.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > type`](#modules_items_anyOf_i1_oneOf_i62_type)
        - [5.1.2.63.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > key`](#modules_items_anyOf_i1_oneOf_i62_key)
        - [5.1.2.63.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyColor`](#modules_items_anyOf_i1_oneOf_i62_keyColor)
        - [5.1.2.63.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyIcon`](#modules_items_anyOf_i1_oneOf_i62_keyIcon)
        - [5.1.2.63.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyWidth`](#modules_items_anyOf_i1_oneOf_i62_keyWidth)
        - [5.1.2.63.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > outputColor`](#modules_items_anyOf_i1_oneOf_i62_outputColor)
        - [5.1.2.63.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > format`](#modules_items_anyOf_i1_oneOf_i62_format)
      - [5.1.2.64. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version`](#modules_items_anyOf_i1_oneOf_i63)
        - [5.1.2.64.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > type`](#modules_items_anyOf_i1_oneOf_i63_type)
        - [5.1.2.64.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > key`](#modules_items_anyOf_i1_oneOf_i63_key)
        - [5.1.2.64.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyColor`](#modules_items_anyOf_i1_oneOf_i63_keyColor)
        - [5.1.2.64.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyIcon`](#modules_items_anyOf_i1_oneOf_i63_keyIcon)
        - [5.1.2.64.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyWidth`](#modules_items_anyOf_i1_oneOf_i63_keyWidth)
        - [5.1.2.64.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > outputColor`](#modules_items_anyOf_i1_oneOf_i63_outputColor)
        - [5.1.2.64.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > format`](#modules_items_anyOf_i1_oneOf_i63_format)
      - [5.1.2.65. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan`](#modules_items_anyOf_i1_oneOf_i64)
        - [5.1.2.65.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > type`](#modules_items_anyOf_i1_oneOf_i64_type)
        - [5.1.2.65.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > key`](#modules_items_anyOf_i1_oneOf_i64_key)
        - [5.1.2.65.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyColor`](#modules_items_anyOf_i1_oneOf_i64_keyColor)
        - [5.1.2.65.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyIcon`](#modules_items_anyOf_i1_oneOf_i64_keyIcon)
        - [5.1.2.65.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyWidth`](#modules_items_anyOf_i1_oneOf_i64_keyWidth)
        - [5.1.2.65.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > outputColor`](#modules_items_anyOf_i1_oneOf_i64_outputColor)
        - [5.1.2.65.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > format`](#modules_items_anyOf_i1_oneOf_i64_format)
      - [5.1.2.66. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper`](#modules_items_anyOf_i1_oneOf_i65)
        - [5.1.2.66.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > type`](#modules_items_anyOf_i1_oneOf_i65_type)
        - [5.1.2.66.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > key`](#modules_items_anyOf_i1_oneOf_i65_key)
        - [5.1.2.66.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyColor`](#modules_items_anyOf_i1_oneOf_i65_keyColor)
        - [5.1.2.66.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyIcon`](#modules_items_anyOf_i1_oneOf_i65_keyIcon)
        - [5.1.2.66.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyWidth`](#modules_items_anyOf_i1_oneOf_i65_keyWidth)
        - [5.1.2.66.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > outputColor`](#modules_items_anyOf_i1_oneOf_i65_outputColor)
        - [5.1.2.66.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > format`](#modules_items_anyOf_i1_oneOf_i65_format)
      - [5.1.2.67. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather`](#modules_items_anyOf_i1_oneOf_i66)
        - [5.1.2.67.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > type`](#modules_items_anyOf_i1_oneOf_i66_type)
        - [5.1.2.67.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > location`](#modules_items_anyOf_i1_oneOf_i66_location)
        - [5.1.2.67.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > timeout`](#modules_items_anyOf_i1_oneOf_i66_timeout)
        - [5.1.2.67.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputFormat`](#modules_items_anyOf_i1_oneOf_i66_outputFormat)
        - [5.1.2.67.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > key`](#modules_items_anyOf_i1_oneOf_i66_key)
        - [5.1.2.67.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyColor`](#modules_items_anyOf_i1_oneOf_i66_keyColor)
        - [5.1.2.67.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyIcon`](#modules_items_anyOf_i1_oneOf_i66_keyIcon)
        - [5.1.2.67.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyWidth`](#modules_items_anyOf_i1_oneOf_i66_keyWidth)
        - [5.1.2.67.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputColor`](#modules_items_anyOf_i1_oneOf_i66_outputColor)
        - [5.1.2.67.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > format`](#modules_items_anyOf_i1_oneOf_i66_format)
      - [5.1.2.68. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi`](#modules_items_anyOf_i1_oneOf_i67)
        - [5.1.2.68.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > type`](#modules_items_anyOf_i1_oneOf_i67_type)
        - [5.1.2.68.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > key`](#modules_items_anyOf_i1_oneOf_i67_key)
        - [5.1.2.68.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyColor`](#modules_items_anyOf_i1_oneOf_i67_keyColor)
        - [5.1.2.68.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyIcon`](#modules_items_anyOf_i1_oneOf_i67_keyIcon)
        - [5.1.2.68.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyWidth`](#modules_items_anyOf_i1_oneOf_i67_keyWidth)
        - [5.1.2.68.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > outputColor`](#modules_items_anyOf_i1_oneOf_i67_outputColor)
        - [5.1.2.68.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > format`](#modules_items_anyOf_i1_oneOf_i67_format)
      - [5.1.2.69. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager`](#modules_items_anyOf_i1_oneOf_i68)
        - [5.1.2.69.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > type`](#modules_items_anyOf_i1_oneOf_i68_type)
        - [5.1.2.69.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > detectPlugin`](#modules_items_anyOf_i1_oneOf_i68_detectPlugin)
        - [5.1.2.69.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > key`](#modules_items_anyOf_i1_oneOf_i68_key)
        - [5.1.2.69.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyColor`](#modules_items_anyOf_i1_oneOf_i68_keyColor)
        - [5.1.2.69.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyIcon`](#modules_items_anyOf_i1_oneOf_i68_keyIcon)
        - [5.1.2.69.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyWidth`](#modules_items_anyOf_i1_oneOf_i68_keyWidth)
        - [5.1.2.69.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > outputColor`](#modules_items_anyOf_i1_oneOf_i68_outputColor)
        - [5.1.2.69.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > format`](#modules_items_anyOf_i1_oneOf_i68_format)
      - [5.1.2.70. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme`](#modules_items_anyOf_i1_oneOf_i69)
        - [5.1.2.70.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > type`](#modules_items_anyOf_i1_oneOf_i69_type)
        - [5.1.2.70.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > key`](#modules_items_anyOf_i1_oneOf_i69_key)
        - [5.1.2.70.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyColor`](#modules_items_anyOf_i1_oneOf_i69_keyColor)
        - [5.1.2.70.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyIcon`](#modules_items_anyOf_i1_oneOf_i69_keyIcon)
        - [5.1.2.70.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyWidth`](#modules_items_anyOf_i1_oneOf_i69_keyWidth)
        - [5.1.2.70.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > outputColor`](#modules_items_anyOf_i1_oneOf_i69_outputColor)
        - [5.1.2.70.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > format`](#modules_items_anyOf_i1_oneOf_i69_format)
      - [5.1.2.71. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool`](#modules_items_anyOf_i1_oneOf_i70)
        - [5.1.2.71.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > type`](#modules_items_anyOf_i1_oneOf_i70_type)
        - [5.1.2.71.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > percent`](#modules_items_anyOf_i1_oneOf_i70_percent)
        - [5.1.2.71.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > key`](#modules_items_anyOf_i1_oneOf_i70_key)
        - [5.1.2.71.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyColor`](#modules_items_anyOf_i1_oneOf_i70_keyColor)
        - [5.1.2.71.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyIcon`](#modules_items_anyOf_i1_oneOf_i70_keyIcon)
        - [5.1.2.71.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyWidth`](#modules_items_anyOf_i1_oneOf_i70_keyWidth)
        - [5.1.2.71.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > outputColor`](#modules_items_anyOf_i1_oneOf_i70_outputColor)
        - [5.1.2.71.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > format`](#modules_items_anyOf_i1_oneOf_i70_format)
      - [5.1.2.72. Property `JSON config > modules > modules items > anyOf > item 1 > type`](#modules_items_anyOf_i1_type)

**Title:** JSON config

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** JSON config file for fastfetch. Usually located at `~/.config/fastfetch/config.jsonc`

| Property               | Pattern | Type        | Deprecated | Definition | Title/Description                                                                                        |
| ---------------------- | ------- | ----------- | ---------- | ---------- | -------------------------------------------------------------------------------------------------------- |
| - [$schema](#schema )  | No      | string      | No         | -          | JSON schema URL, for JSON validation and IDE intelligence                                                |
| - [logo](#logo )       | No      | Combination | No         | -          | Fastfetch logo configurations<br />See also https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options |
| - [general](#general ) | No      | object      | No         | -          | Fastfetch general configurations                                                                         |
| - [display](#display ) | No      | object      | No         | -          | Configure how things should be displayed                                                                 |
| - [modules](#modules ) | No      | array       | No         | -          | Fastfetch modules to run                                                                                 |

## <a name="schema"></a>1. Property `JSON config > $schema`

|              |                                                                             |
| ------------ | --------------------------------------------------------------------------- |
| **Type**     | `string`                                                                    |
| **Required** | No                                                                          |
| **Format**   | `uri`                                                                       |
| **Default**  | `"https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json"` |

**Description:** JSON schema URL, for JSON validation and IDE intelligence

## <a name="logo"></a>2. Property `JSON config > logo`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Fastfetch logo configurations
See also https://github.com/fastfetch-cli/fastfetch/wiki/Logo-options

| One of(Option)           |
| ------------------------ |
| [item 0](#logo_oneOf_i0) |
| [item 1](#logo_oneOf_i1) |
| [item 2](#logo_oneOf_i2) |

### <a name="logo_oneOf_i0"></a>2.1. Property `JSON config > logo > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Disable logo

Specific value: `null`

### <a name="logo_oneOf_i1"></a>2.2. Property `JSON config > logo > oneOf > item 1`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the source file of the logo

### <a name="logo_oneOf_i2"></a>2.3. Property `JSON config > logo > oneOf > item 2`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Fastfetch logo configurations

| Property                                                     | Pattern | Type             | Deprecated | Definition | Title/Description                                                                        |
| ------------------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------------------------------------------------- |
| - [type](#logo_oneOf_i2_type )                               | No      | enum (of string) | No         | -          | Set the type of the logo                                                                 |
| - [source](#logo_oneOf_i2_source )                           | No      | string           | No         | -          | Set the source file of the logo                                                          |
| - [color](#logo_oneOf_i2_color )                             | No      | object           | No         | -          | Override colors in the logo                                                              |
| - [width](#logo_oneOf_i2_width )                             | No      | integer          | No         | -          | Set the width of the logo (in characters). Required for iTerm image protocol             |
| - [height](#logo_oneOf_i2_height )                           | No      | integer          | No         | -          | Set the height of the logo (in characters). Required for iTerm image protocol            |
| - [padding](#logo_oneOf_i2_padding )                         | No      | object           | No         | -          | Set the padding of the logo                                                              |
| - [printRemaining](#logo_oneOf_i2_printRemaining )           | No      | boolean          | No         | -          | Whether to print the remaining logo if it has more lines than modules to display         |
| - [preserveAspectRatio](#logo_oneOf_i2_preserveAspectRatio ) | No      | boolean          | No         | -          | Whether to preserve the aspect ratio of the logo. Supported by iTerm image protocol only |
| - [recache](#logo_oneOf_i2_recache )                         | No      | boolean          | No         | -          | If true, regenerate image logo cache                                                     |
| - [position](#logo_oneOf_i2_position )                       | No      | enum (of string) | No         | -          | Set the position where the logo should be displayed                                      |
| - [chafa](#logo_oneOf_i2_chafa )                             | No      | object           | No         | -          | Chafa configuration. See chafa documentation for details                                 |

#### <a name="logo_oneOf_i2_type"></a>2.3.1. Property `JSON config > logo > oneOf > item 2 > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"auto"`           |

**Description:** Set the type of the logo

Must be one of:
* "auto"
* "builtin"
* "small"
* "file"
* "file-raw"
* "data"
* "data-raw"
* "sixel"
* "kitty"
* "kitty-direct"
* "kitty-icat"
* "iterm"
* "chafa"
* "raw"
* "none"

#### <a name="logo_oneOf_i2_source"></a>2.3.2. Property `JSON config > logo > oneOf > item 2 > source`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the source file of the logo

#### <a name="logo_oneOf_i2_color"></a>2.3.3. Property `JSON config > logo > oneOf > item 2 > color`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Override colors in the logo

| Property                       | Pattern | Type             | Deprecated | Definition                           | Title/Description |
| ------------------------------ | ------- | ---------------- | ---------- | ------------------------------------ | ----------------- |
| - [1](#logo_oneOf_i2_color_1 ) | No      | enum (of string) | No         | In #/$defs/colors                    | Color 1           |
| - [2](#logo_oneOf_i2_color_2 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 2           |
| - [3](#logo_oneOf_i2_color_3 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 3           |
| - [4](#logo_oneOf_i2_color_4 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 4           |
| - [5](#logo_oneOf_i2_color_5 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 5           |
| - [6](#logo_oneOf_i2_color_6 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 6           |
| - [7](#logo_oneOf_i2_color_7 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 7           |
| - [8](#logo_oneOf_i2_color_8 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 8           |
| - [9](#logo_oneOf_i2_color_9 ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Color 9           |

##### <a name="logo_oneOf_i2_color_1"></a>2.3.3.1. Property `JSON config > logo > oneOf > item 2 > color > 1`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Defined in** | #/$defs/colors     |

**Description:** Color 1

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

##### <a name="logo_oneOf_i2_color_2"></a>2.3.3.2. Property `JSON config > logo > oneOf > item 2 > color > 2`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 2

##### <a name="logo_oneOf_i2_color_3"></a>2.3.3.3. Property `JSON config > logo > oneOf > item 2 > color > 3`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 3

##### <a name="logo_oneOf_i2_color_4"></a>2.3.3.4. Property `JSON config > logo > oneOf > item 2 > color > 4`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 4

##### <a name="logo_oneOf_i2_color_5"></a>2.3.3.5. Property `JSON config > logo > oneOf > item 2 > color > 5`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 5

##### <a name="logo_oneOf_i2_color_6"></a>2.3.3.6. Property `JSON config > logo > oneOf > item 2 > color > 6`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 6

##### <a name="logo_oneOf_i2_color_7"></a>2.3.3.7. Property `JSON config > logo > oneOf > item 2 > color > 7`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 7

##### <a name="logo_oneOf_i2_color_8"></a>2.3.3.8. Property `JSON config > logo > oneOf > item 2 > color > 8`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 8

##### <a name="logo_oneOf_i2_color_9"></a>2.3.3.9. Property `JSON config > logo > oneOf > item 2 > color > 9`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Color 9

#### <a name="logo_oneOf_i2_width"></a>2.3.4. Property `JSON config > logo > oneOf > item 2 > width`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the width of the logo (in characters). Required for iTerm image protocol

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

#### <a name="logo_oneOf_i2_height"></a>2.3.5. Property `JSON config > logo > oneOf > item 2 > height`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the height of the logo (in characters). Required for iTerm image protocol

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

#### <a name="logo_oneOf_i2_padding"></a>2.3.6. Property `JSON config > logo > oneOf > item 2 > padding`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set the padding of the logo

| Property                                 | Pattern | Type    | Deprecated | Definition | Title/Description                 |
| ---------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------------------- |
| - [top](#logo_oneOf_i2_padding_top )     | No      | integer | No         | -          | Set the top padding of the logo   |
| - [left](#logo_oneOf_i2_padding_left )   | No      | integer | No         | -          | Set the left padding of the logo  |
| - [right](#logo_oneOf_i2_padding_right ) | No      | integer | No         | -          | Set the right padding of the logo |

##### <a name="logo_oneOf_i2_padding_top"></a>2.3.6.1. Property `JSON config > logo > oneOf > item 2 > padding > top`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the top padding of the logo

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

##### <a name="logo_oneOf_i2_padding_left"></a>2.3.6.2. Property `JSON config > logo > oneOf > item 2 > padding > left`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the left padding of the logo

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

##### <a name="logo_oneOf_i2_padding_right"></a>2.3.6.3. Property `JSON config > logo > oneOf > item 2 > padding > right`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Set the right padding of the logo

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

#### <a name="logo_oneOf_i2_printRemaining"></a>2.3.7. Property `JSON config > logo > oneOf > item 2 > printRemaining`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to print the remaining logo if it has more lines than modules to display

#### <a name="logo_oneOf_i2_preserveAspectRatio"></a>2.3.8. Property `JSON config > logo > oneOf > item 2 > preserveAspectRatio`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to preserve the aspect ratio of the logo. Supported by iTerm image protocol only

#### <a name="logo_oneOf_i2_recache"></a>2.3.9. Property `JSON config > logo > oneOf > item 2 > recache`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** If true, regenerate image logo cache

#### <a name="logo_oneOf_i2_position"></a>2.3.10. Property `JSON config > logo > oneOf > item 2 > position`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"left"`           |

**Description:** Set the position where the logo should be displayed

Must be one of:
* "left"
* "top"
* "right"

#### <a name="logo_oneOf_i2_chafa"></a>2.3.11. Property `JSON config > logo > oneOf > item 2 > chafa`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Chafa configuration. See chafa documentation for details

| Property                                         | Pattern | Type             | Deprecated | Definition | Title/Description                                                                              |
| ------------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------------------------------------------------------- |
| - [fgOnly](#logo_oneOf_i2_chafa_fgOnly )         | No      | boolean          | No         | -          | Produce character-cell output using foreground colors only                                     |
| - [symbols](#logo_oneOf_i2_chafa_symbols )       | No      | string           | No         | -          | Specify character symbols to employ in final output                                            |
| - [canvasMode](#logo_oneOf_i2_chafa_canvasMode ) | No      | enum (of string) | No         | -          | Determine how colors are used in the output. This value maps to enum ChafaCanvasMode.          |
| - [colorSpace](#logo_oneOf_i2_chafa_colorSpace ) | No      | enum (of string) | No         | -          | Set color space used for quantization. This value maps to enum ChafaColorSpace.                |
| - [ditherMode](#logo_oneOf_i2_chafa_ditherMode ) | No      | enum (of string) | No         | -          | Set output dither mode (No effect with 24-bit color). This value maps to enum ChafaDitherMode. |

##### <a name="logo_oneOf_i2_chafa_fgOnly"></a>2.3.11.1. Property `JSON config > logo > oneOf > item 2 > chafa > fgOnly`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Produce character-cell output using foreground colors only

##### <a name="logo_oneOf_i2_chafa_symbols"></a>2.3.11.2. Property `JSON config > logo > oneOf > item 2 > chafa > symbols`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Specify character symbols to employ in final output

##### <a name="logo_oneOf_i2_chafa_canvasMode"></a>2.3.11.3. Property `JSON config > logo > oneOf > item 2 > chafa > canvasMode`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Determine how colors are used in the output. This value maps to enum ChafaCanvasMode.

Must be one of:
* "TRUECOLOR"
* "INDEXED_256"
* "INDEXED_240"
* "INDEXED_16"
* "FGBG_BGFG"
* "FGBG"
* "INDEXED_8"
* "INDEXED_16_8"

##### <a name="logo_oneOf_i2_chafa_colorSpace"></a>2.3.11.4. Property `JSON config > logo > oneOf > item 2 > chafa > colorSpace`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Set color space used for quantization. This value maps to enum ChafaColorSpace.

Must be one of:
* "RGB"
* "DIN99D"

##### <a name="logo_oneOf_i2_chafa_ditherMode"></a>2.3.11.5. Property `JSON config > logo > oneOf > item 2 > chafa > ditherMode`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Set output dither mode (No effect with 24-bit color). This value maps to enum ChafaDitherMode.

Must be one of:
* "NONE"
* "ORDERED"
* "DIFFUSION"

## <a name="general"></a>3. Property `JSON config > general`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Fastfetch general configurations

| Property                                           | Pattern | Type        | Deprecated | Definition | Title/Description                                                            |
| -------------------------------------------------- | ------- | ----------- | ---------- | ---------- | ---------------------------------------------------------------------------- |
| - [thread](#general_thread )                       | No      | boolean     | No         | -          | Use separate threads for HTTP requests                                       |
| - [escapeBedrock](#general_escapeBedrock )         | No      | boolean     | No         | -          | On Bedrock Linux, whether to escape the bedrock jail                         |
| - [playerName](#general_playerName )               | No      | string      | No         | -          | The name of the player to use for Media and Player modules. Linux only       |
| - [dsForceDrm](#general_dsForceDrm )               | No      | Combination | No         | -          | Force display detection to use DRM. Linux only                               |
| - [wmiTimeout](#general_wmiTimeout )               | No      | integer     | No         | -          | Set the timeout (ms) for WMI queries, \`-1\` for no timeout. Windows only    |
| - [processingTimeout](#general_processingTimeout ) | No      | integer     | No         | -          | Set the timeout (ms) when waiting for child processes, \`-1\` for no timeout |
| - [preRun](#general_preRun )                       | No      | string      | No         | -          | Set the command to be executed before printing logos                         |
| - [detectVersion](#general_detectVersion )         | No      | boolean     | No         | -          | Whether to detect and display component versions. Mainly for benchmarking    |

### <a name="general_thread"></a>3.1. Property `JSON config > general > thread`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Use separate threads for HTTP requests

### <a name="general_escapeBedrock"></a>3.2. Property `JSON config > general > escapeBedrock`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** On Bedrock Linux, whether to escape the bedrock jail

### <a name="general_playerName"></a>3.3. Property `JSON config > general > playerName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The name of the player to use for Media and Player modules. Linux only

### <a name="general_dsForceDrm"></a>3.4. Property `JSON config > general > dsForceDrm`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Default**               | `false`          |

**Description:** Force display detection to use DRM. Linux only

| One of(Option)                         |
| -------------------------------------- |
| [item 0](#general_dsForceDrm_oneOf_i0) |
| [item 1](#general_dsForceDrm_oneOf_i1) |
| [item 2](#general_dsForceDrm_oneOf_i2) |

#### <a name="general_dsForceDrm_oneOf_i0"></a>3.4.1. Property `JSON config > general > dsForceDrm > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Try `wayland`, then `x11`, then `drm`

Specific value: `false`

#### <a name="general_dsForceDrm_oneOf_i1"></a>3.4.2. Property `JSON config > general > dsForceDrm > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Use `/sys/class/drm` only

Specific value: `"sysfs-only"`

#### <a name="general_dsForceDrm_oneOf_i2"></a>3.4.3. Property `JSON config > general > dsForceDrm > oneOf > item 2`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Try `libdrm` first, then `sysfs` if libdrm fails

Specific value: `true`

### <a name="general_wmiTimeout"></a>3.5. Property `JSON config > general > wmiTimeout`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `5000`    |

**Description:** Set the timeout (ms) for WMI queries, `-1` for no timeout. Windows only

### <a name="general_processingTimeout"></a>3.6. Property `JSON config > general > processingTimeout`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `5000`    |

**Description:** Set the timeout (ms) when waiting for child processes, `-1` for no timeout

### <a name="general_preRun"></a>3.7. Property `JSON config > general > preRun`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `""`     |

**Description:** Set the command to be executed before printing logos

### <a name="general_detectVersion"></a>3.8. Property `JSON config > general > detectVersion`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to detect and display component versions. Mainly for benchmarking

## <a name="display"></a>4. Property `JSON config > display`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Configure how things should be displayed

| Property                                       | Pattern | Type            | Deprecated | Definition | Title/Description                                                       |
| ---------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------------------------------------------------------------- |
| - [stat](#display_stat )                       | No      | Combination     | No         | -          | Show time usage (in ms) for individual modules with optional threshold  |
| - [pipe](#display_pipe )                       | No      | boolean         | No         | -          | Whether to disable colors (auto-detected based on isatty(1) by default) |
| - [showErrors](#display_showErrors )           | No      | boolean         | No         | -          | Print occurring errors to the console. False to ignore errored modules  |
| - [disableLinewrap](#display_disableLinewrap ) | No      | boolean         | No         | -          | Whether to disable line wrap during execution                           |
| - [hideCursor](#display_hideCursor )           | No      | boolean         | No         | -          | Whether to hide the cursor during execution                             |
| - [separator](#display_separator )             | No      | string          | No         | -          | Set the separator between key and value                                 |
| - [color](#display_color )                     | No      | Combination     | No         | -          | Set the color of the keys and title                                     |
| - [brightColor](#display_brightColor )         | No      | boolean         | No         | -          | Set if the keys, title and ASCII logo should be printed in bright color |
| - [key](#display_key )                         | No      | object          | No         | -          | Set how module keys should be displayed                                 |
| - [size](#display_size )                       | No      | object          | No         | -          | Set how size values should be displayed                                 |
| - [temp](#display_temp )                       | No      | object          | No         | -          | Set how temperature values should be displayed                          |
| - [bar](#display_bar )                         | No      | object          | No         | -          | Set the bar configuration                                               |
| - [percent](#display_percent )                 | No      | object          | No         | -          | Set how percentage values should be displayed                           |
| - [freq](#display_freq )                       | No      | object          | No         | -          | Set how frequency values should be displayed                            |
| - [noBuffer](#display_noBuffer )               | No      | boolean         | No         | -          | Whether to disable the stdout application buffer                        |
| - [constants](#display_constants )             | No      | array of string | No         | -          | List of strings to be used in custom format of modules                  |

### <a name="display_stat"></a>4.1. Property `JSON config > display > stat`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Show time usage (in ms) for individual modules with optional threshold

| One of(Option)                   |
| -------------------------------- |
| [item 0](#display_stat_oneOf_i0) |
| [item 1](#display_stat_oneOf_i1) |

#### <a name="display_stat_oneOf_i0"></a>4.1.1. Property `JSON config > display > stat > oneOf > item 0`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

#### <a name="display_stat_oneOf_i1"></a>4.1.2. Property `JSON config > display > stat > oneOf > item 1`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

### <a name="display_pipe"></a>4.2. Property `JSON config > display > pipe`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to disable colors (auto-detected based on isatty(1) by default)

### <a name="display_showErrors"></a>4.3. Property `JSON config > display > showErrors`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Print occurring errors to the console. False to ignore errored modules

### <a name="display_disableLinewrap"></a>4.4. Property `JSON config > display > disableLinewrap`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to disable line wrap during execution

### <a name="display_hideCursor"></a>4.5. Property `JSON config > display > hideCursor`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Whether to hide the cursor during execution

### <a name="display_separator"></a>4.6. Property `JSON config > display > separator`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `": "`   |

**Description:** Set the separator between key and value

### <a name="display_color"></a>4.7. Property `JSON config > display > color`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Set the color of the keys and title

| One of(Option)                    |
| --------------------------------- |
| [colors](#display_color_oneOf_i0) |
| [item 1](#display_color_oneOf_i1) |

#### <a name="display_color_oneOf_i0"></a>4.7.1. Property `JSON config > display > color > oneOf > colors`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set both the colors of keys and title

#### <a name="display_color_oneOf_i1"></a>4.7.2. Property `JSON config > display > color > oneOf > item 1`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                          | Pattern | Type             | Deprecated | Definition                           | Title/Description                        |
| ------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------ | ---------------------------------------- |
| - [keys](#display_color_oneOf_i1_keys )           | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set the color of the keys                |
| - [title](#display_color_oneOf_i1_title )         | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set the color of the title               |
| - [output](#display_color_oneOf_i1_output )       | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set the color of the module output       |
| - [separator](#display_color_oneOf_i1_separator ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set the color of the key-value separator |

##### <a name="display_color_oneOf_i1_keys"></a>4.7.2.1. Property `JSON config > display > color > oneOf > item 1 > keys`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the keys

##### <a name="display_color_oneOf_i1_title"></a>4.7.2.2. Property `JSON config > display > color > oneOf > item 1 > title`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the title

##### <a name="display_color_oneOf_i1_output"></a>4.7.2.3. Property `JSON config > display > color > oneOf > item 1 > output`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the module output

##### <a name="display_color_oneOf_i1_separator"></a>4.7.2.4. Property `JSON config > display > color > oneOf > item 1 > separator`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set the color of the key-value separator

### <a name="display_brightColor"></a>4.8. Property `JSON config > display > brightColor`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Set if the keys, title and ASCII logo should be printed in bright color

### <a name="display_key"></a>4.9. Property `JSON config > display > key`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how module keys should be displayed

| Property                                   | Pattern | Type             | Deprecated | Definition | Title/Description                                             |
| ------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------------- |
| - [width](#display_key_width )             | No      | integer          | No         | -          | Align the width of keys to number of characters, 0 to disable |
| - [type](#display_key_type )               | No      | enum (of string) | No         | -          | Set whether to show icon before string keys                   |
| - [paddingLeft](#display_key_paddingLeft ) | No      | integer          | No         | -          | Set the left padding of keys                                  |

#### <a name="display_key_width"></a>4.9.1. Property `JSON config > display > key > width`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Align the width of keys to number of characters, 0 to disable

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

#### <a name="display_key_type"></a>4.9.2. Property `JSON config > display > key > type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"string"`         |

**Description:** Set whether to show icon before string keys

Must be one of:
* "none"
* "string"
* "icon"
* "both"

#### <a name="display_key_paddingLeft"></a>4.9.3. Property `JSON config > display > key > paddingLeft`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Set the left padding of keys

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

### <a name="display_size"></a>4.10. Property `JSON config > display > size`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how size values should be displayed

| Property                                      | Pattern | Type             | Deprecated | Definition | Title/Description                                                              |
| --------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------------------------------ |
| - [binaryPrefix](#display_size_binaryPrefix ) | No      | Combination      | No         | -          | Set the binary prefix to use when formatting sizes                             |
| - [maxPrefix](#display_size_maxPrefix )       | No      | enum (of string) | No         | -          | Set the largest binary prefix to use when formatting sizes                     |
| - [ndigits](#display_size_ndigits )           | No      | integer          | No         | -          | Set the number of digits to keep after the decimal point when formatting sizes |

#### <a name="display_size_binaryPrefix"></a>4.10.1. Property `JSON config > display > size > binaryPrefix`

|              |             |
| ------------ | ----------- |
| **Type**     | `combining` |
| **Required** | No          |
| **Default**  | `"iec"`     |

**Description:** Set the binary prefix to use when formatting sizes

| One of(Option)                                |
| --------------------------------------------- |
| [item 0](#display_size_binaryPrefix_oneOf_i0) |
| [item 1](#display_size_binaryPrefix_oneOf_i1) |
| [item 2](#display_size_binaryPrefix_oneOf_i2) |

##### <a name="display_size_binaryPrefix_oneOf_i0"></a>4.10.1.1. Property `JSON config > display > size > binaryPrefix > oneOf > item 0`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** 1024 Bytes = 1 KiB, 1024 KiB = 1 MiB, ... (standard)

Specific value: `"iec"`

##### <a name="display_size_binaryPrefix_oneOf_i1"></a>4.10.1.2. Property `JSON config > display > size > binaryPrefix > oneOf > item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** 1000 Bytes = 1 kB, 1000 kB = 1 MB, ...

Specific value: `"si"`

##### <a name="display_size_binaryPrefix_oneOf_i2"></a>4.10.1.3. Property `JSON config > display > size > binaryPrefix > oneOf > item 2`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** 1024 Bytes = 1 KB, 1024 KB = 1 MB, ...

Specific value: `"jedec"`

#### <a name="display_size_maxPrefix"></a>4.10.2. Property `JSON config > display > size > maxPrefix`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"YB"`             |

**Description:** Set the largest binary prefix to use when formatting sizes

Must be one of:
* "B"
* "kB"
* "MB"
* "GB"
* "TB"
* "PB"
* "EB"
* "ZB"
* "YB"

#### <a name="display_size_ndigits"></a>4.10.3. Property `JSON config > display > size > ndigits`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `2`       |

**Description:** Set the number of digits to keep after the decimal point when formatting sizes

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

### <a name="display_temp"></a>4.11. Property `JSON config > display > temp`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how temperature values should be displayed

| Property                            | Pattern | Type             | Deprecated | Definition | Title/Description                                                                           |
| ----------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------------------------------------------- |
| - [unit](#display_temp_unit )       | No      | enum (of string) | No         | -          | Set the unit of temperature                                                                 |
| - [ndigits](#display_temp_ndigits ) | No      | integer          | No         | -          | Set the number of digits to keep after the decimal point when formatting temperature values |
| - [color](#display_temp_color )     | No      | object           | No         | -          | Set colors used in different states of temperature values                                   |

#### <a name="display_temp_unit"></a>4.11.1. Property `JSON config > display > temp > unit`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"D"`              |

**Description:** Set the unit of temperature

Must be one of:
* "D"
* "Default"
* "Celsius"
* "C"
* "Fahrenheit"
* "F"
* "Kelvin"
* "K"

#### <a name="display_temp_ndigits"></a>4.11.2. Property `JSON config > display > temp > ndigits`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `1`       |

**Description:** Set the number of digits to keep after the decimal point when formatting temperature values

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

#### <a name="display_temp_color"></a>4.11.3. Property `JSON config > display > temp > color`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set colors used in different states of temperature values

| Property                                | Pattern | Type             | Deprecated | Definition        | Title/Description          |
| --------------------------------------- | ------- | ---------------- | ---------- | ----------------- | -------------------------- |
| - [green](#display_temp_color_green )   | No      | enum (of string) | No         | In #/$defs/colors | Color used in green state  |
| - [yellow](#display_temp_color_yellow ) | No      | enum (of string) | No         | In #/$defs/colors | Color used in yellow state |
| - [red](#display_temp_color_red )       | No      | enum (of string) | No         | In #/$defs/colors | Color used in red state    |

##### <a name="display_temp_color_green"></a>4.11.3.1. Property `JSON config > display > temp > color > green`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"green"`          |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in green state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

##### <a name="display_temp_color_yellow"></a>4.11.3.2. Property `JSON config > display > temp > color > yellow`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_yellow"`   |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in yellow state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

##### <a name="display_temp_color_red"></a>4.11.3.3. Property `JSON config > display > temp > color > red`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_red"`      |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in red state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

### <a name="display_bar"></a>4.12. Property `JSON config > display > bar`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set the bar configuration

| Property                                   | Pattern | Type    | Deprecated | Definition | Title/Description                                 |
| ------------------------------------------ | ------- | ------- | ---------- | ---------- | ------------------------------------------------- |
| - [charElapsed](#display_bar_charElapsed ) | No      | string  | No         | -          | Set the character to use in elapsed part          |
| - [charTotal](#display_bar_charTotal )     | No      | string  | No         | -          | Set the character to use in total part            |
| - [borderLeft](#display_bar_borderLeft )   | No      | string  | No         | -          | Set the string to use at left border              |
| - [borderRight](#display_bar_borderRight ) | No      | string  | No         | -          | Set the string to use at right border             |
| - [width](#display_bar_width )             | No      | integer | No         | -          | Set the width of the bar, in number of characters |

#### <a name="display_bar_charElapsed"></a>4.12.1. Property `JSON config > display > bar > charElapsed`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"■"`    |

**Description:** Set the character to use in elapsed part

#### <a name="display_bar_charTotal"></a>4.12.2. Property `JSON config > display > bar > charTotal`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"-"`    |

**Description:** Set the character to use in total part

#### <a name="display_bar_borderLeft"></a>4.12.3. Property `JSON config > display > bar > borderLeft`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"[ "`   |

**Description:** Set the string to use at left border

#### <a name="display_bar_borderRight"></a>4.12.4. Property `JSON config > display > bar > borderRight`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `" ]"`   |

**Description:** Set the string to use at right border

#### <a name="display_bar_width"></a>4.12.5. Property `JSON config > display > bar > width`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `10`      |

**Description:** Set the width of the bar, in number of characters

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

### <a name="display_percent"></a>4.13. Property `JSON config > display > percent`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how percentage values should be displayed

| Property                               | Pattern | Type   | Deprecated | Definition             | Title/Description                                                                           |
| -------------------------------------- | ------- | ------ | ---------- | ---------------------- | ------------------------------------------------------------------------------------------- |
| - [type](#display_percent_type )       | No      | object | No         | In #/$defs/percentType | Set the percentage output type                                                              |
| - [ndigits](#display_percent_ndigits ) | No      | number | No         | -                      | Set the number of digits to keep after the decimal point when formatting percentage numbers |
| - [color](#display_percent_color )     | No      | object | No         | -                      | Set colors used in different states of percentage bars and numbers                          |

#### <a name="display_percent_type"></a>4.13.1. Property `JSON config > display > percent > type`

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `combining`         |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/percentType |

**Description:** Set the percentage output type

| One of(Option)                           |
| ---------------------------------------- |
| [item 0](#display_percent_type_oneOf_i0) |
| [item 1](#display_percent_type_oneOf_i1) |

##### <a name="display_percent_type_oneOf_i0"></a>4.13.1.1. Property `JSON config > display > percent > type > oneOf > item 0`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `9`      |

**Description:** 0 to use global setting, 1 for percentage number, 2 for multi-color bar, 3 for both, 6 for bar only, 9 for colored number, 10 for monochrome bar

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 255 |

##### <a name="display_percent_type_oneOf_i1"></a>4.13.1.2. Property `JSON config > display > percent > type > oneOf > item 1`

|              |                             |
| ------------ | --------------------------- |
| **Type**     | `array of enum (of string)` |
| **Required** | No                          |
| **Default**  | `["num", "num-color"]`      |

**Description:** Array of string flags

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                      | Description |
| ---------------------------------------------------- | ----------- |
| [item 1 items](#display_percent_type_oneOf_i1_items) | -           |

###### <a name="display_percent_type_oneOf_i1_items"></a>4.13.1.2.1. JSON config > display > percent > type > oneOf > item 1 > item 1 items

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "num"
* "bar"
* "hide-others"
* "num-color"
* "bar-monochrome"

#### <a name="display_percent_ndigits"></a>4.13.2. Property `JSON config > display > percent > ndigits`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |
| **Default**  | `0`      |

**Description:** Set the number of digits to keep after the decimal point when formatting percentage numbers

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

#### <a name="display_percent_color"></a>4.13.3. Property `JSON config > display > percent > color`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set colors used in different states of percentage bars and numbers

| Property                                   | Pattern | Type             | Deprecated | Definition        | Title/Description          |
| ------------------------------------------ | ------- | ---------------- | ---------- | ----------------- | -------------------------- |
| - [green](#display_percent_color_green )   | No      | enum (of string) | No         | In #/$defs/colors | Color used in green state  |
| - [yellow](#display_percent_color_yellow ) | No      | enum (of string) | No         | In #/$defs/colors | Color used in yellow state |
| - [red](#display_percent_color_red )       | No      | enum (of string) | No         | In #/$defs/colors | Color used in red state    |

##### <a name="display_percent_color_green"></a>4.13.3.1. Property `JSON config > display > percent > color > green`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"green"`          |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in green state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

##### <a name="display_percent_color_yellow"></a>4.13.3.2. Property `JSON config > display > percent > color > yellow`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_yellow"`   |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in yellow state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

##### <a name="display_percent_color_red"></a>4.13.3.3. Property `JSON config > display > percent > color > red`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"light_red"`      |
| **Defined in** | #/$defs/colors     |

**Description:** Color used in red state

Must be one of:
* "reset_"
* "bright_"
* "dim_"
* "italic_"
* "underline_"
* "blink_"
* "inverse_"
* "hidden_"
* "strike_"
* "light_"
* "black"
* "red"
* "green"
* "yellow"
* "blue"
* "magenta"
* "cyan"
* "white"
* "default"

### <a name="display_freq"></a>4.14. Property `JSON config > display > freq`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set how frequency values should be displayed

| Property                            | Pattern | Type    | Deprecated | Definition | Title/Description                                                                                                                                                                                  |
| ----------------------------------- | ------- | ------- | ---------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [ndigits](#display_freq_ndigits ) | No      | integer | No         | -          | Set the number of digits to keep after the decimal point when formatting frequency values<br />A positive value will show the frequency in GHz with decimal<br />-1 will show the frequency in MHz |

#### <a name="display_freq_ndigits"></a>4.14.1. Property `JSON config > display > freq > ndigits`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `2`       |

**Description:** Set the number of digits to keep after the decimal point when formatting frequency values
A positive value will show the frequency in GHz with decimal
-1 will show the frequency in MHz

| Restrictions |         |
| ------------ | ------- |
| **Minimum**  | &ge; -1 |
| **Maximum**  | &le; 9  |

### <a name="display_noBuffer"></a>4.15. Property `JSON config > display > noBuffer`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to disable the stdout application buffer

### <a name="display_constants"></a>4.16. Property `JSON config > display > constants`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** List of strings to be used in custom format of modules

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be             | Description |
| ------------------------------------------- | ----------- |
| [constants items](#display_constants_items) | -           |

#### <a name="display_constants_items"></a>4.16.1. JSON config > display > constants > constants items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="modules"></a>5. Property `JSON config > modules`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** Fastfetch modules to run

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [modules items](#modules_items) | -           |

### <a name="modules_items"></a>5.1. JSON config > modules > modules items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                    |
| --------------------------------- |
| [item 0](#modules_items_anyOf_i0) |
| [item 1](#modules_items_anyOf_i1) |

#### <a name="modules_items_anyOf_i0"></a>5.1.1. Property `JSON config > modules > modules items > anyOf > item 0`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** Run module with default configurations

Must be one of:
* "battery"
* "bios"
* "bluetooth"
* "bluetoothradio"
* "board"
* "bootmgr"
* "break"
* "brightness"
* "btrfs"
* "camera"
* "chassis"
* "cpu"
* "cpucache"
* "cpuusage"
* "command"
* "colors"
* "cursor"
* "datetime"
* "display"
* "disk"
* "diskio"
* "de"
* "dns"
* "editor"
* "font"
* "gamepad"
* "gpu"
* "host"
* "icons"
* "initsystem"
* "kernel"
* "lm"
* "loadavg"
* "locale"
* "localip"
* "media"
* "memory"
* "monitor"
* "netio"
* "opencl"
* "opengl"
* "os"
* "packages"
* "physicaldisk"
* "physicalmemory"
* "player"
* "poweradapter"
* "processes"
* "publicip"
* "separator"
* "shell"
* "sound"
* "swap"
* "terminal"
* "terminalfont"
* "terminalsize"
* "terminaltheme"
* "title"
* "theme"
* "tpm"
* "uptime"
* "users"
* "version"
* "vulkan"
* "wallpaper"
* "weather"
* "wm"
* "wifi"
* "wmtheme"
* "zpool"

#### <a name="modules_items_anyOf_i1"></a>5.1.2. Property `JSON config > modules > modules items > anyOf > item 1`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Run module with custom configurations

| Property                                | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [type](#modules_items_anyOf_i1_type ) | No      | string | No         | -          | -                 |

| One of(Option)                                           |
| -------------------------------------------------------- |
| [Break](#modules_items_anyOf_i1_oneOf_i0)                |
| [Battery](#modules_items_anyOf_i1_oneOf_i1)              |
| [BIOS](#modules_items_anyOf_i1_oneOf_i2)                 |
| [Bluetooth](#modules_items_anyOf_i1_oneOf_i3)            |
| [Bluetooth Radio](#modules_items_anyOf_i1_oneOf_i4)      |
| [Board](#modules_items_anyOf_i1_oneOf_i5)                |
| [Boot Manager](#modules_items_anyOf_i1_oneOf_i6)         |
| [Brightness](#modules_items_anyOf_i1_oneOf_i7)           |
| [BTRFS](#modules_items_anyOf_i1_oneOf_i8)                |
| [Camera](#modules_items_anyOf_i1_oneOf_i9)               |
| [Chassis](#modules_items_anyOf_i1_oneOf_i10)             |
| [CPU](#modules_items_anyOf_i1_oneOf_i11)                 |
| [CPU Cache](#modules_items_anyOf_i1_oneOf_i12)           |
| [CPU Usage](#modules_items_anyOf_i1_oneOf_i13)           |
| [Colors](#modules_items_anyOf_i1_oneOf_i14)              |
| [Command](#modules_items_anyOf_i1_oneOf_i15)             |
| [Cursor](#modules_items_anyOf_i1_oneOf_i16)              |
| [Custom](#modules_items_anyOf_i1_oneOf_i17)              |
| [Date Time](#modules_items_anyOf_i1_oneOf_i18)           |
| [Display](#modules_items_anyOf_i1_oneOf_i19)             |
| [Disk](#modules_items_anyOf_i1_oneOf_i20)                |
| [DiskIO](#modules_items_anyOf_i1_oneOf_i21)              |
| [Desktop Environment](#modules_items_anyOf_i1_oneOf_i22) |
| [DNS](#modules_items_anyOf_i1_oneOf_i23)                 |
| [Editor](#modules_items_anyOf_i1_oneOf_i24)              |
| [Font](#modules_items_anyOf_i1_oneOf_i25)                |
| [Gamepad](#modules_items_anyOf_i1_oneOf_i26)             |
| [GPU](#modules_items_anyOf_i1_oneOf_i27)                 |
| [Host](#modules_items_anyOf_i1_oneOf_i28)                |
| [Icons](#modules_items_anyOf_i1_oneOf_i29)               |
| [Init System](#modules_items_anyOf_i1_oneOf_i30)         |
| [Kernel](#modules_items_anyOf_i1_oneOf_i31)              |
| [Login Manager](#modules_items_anyOf_i1_oneOf_i32)       |
| [Local IP](#modules_items_anyOf_i1_oneOf_i33)            |
| [Loadavg](#modules_items_anyOf_i1_oneOf_i34)             |
| [Locale](#modules_items_anyOf_i1_oneOf_i35)              |
| [Media](#modules_items_anyOf_i1_oneOf_i36)               |
| [Memory](#modules_items_anyOf_i1_oneOf_i37)              |
| [Monitor](#modules_items_anyOf_i1_oneOf_i38)             |
| [NetIO](#modules_items_anyOf_i1_oneOf_i39)               |
| [OpenCL](#modules_items_anyOf_i1_oneOf_i40)              |
| [OpenGL](#modules_items_anyOf_i1_oneOf_i41)              |
| [Operating System](#modules_items_anyOf_i1_oneOf_i42)    |
| [Packages](#modules_items_anyOf_i1_oneOf_i43)            |
| [Physical Disk](#modules_items_anyOf_i1_oneOf_i44)       |
| [Physical Memory](#modules_items_anyOf_i1_oneOf_i45)     |
| [Player](#modules_items_anyOf_i1_oneOf_i46)              |
| [Power Adapter](#modules_items_anyOf_i1_oneOf_i47)       |
| [Processes](#modules_items_anyOf_i1_oneOf_i48)           |
| [Public IP](#modules_items_anyOf_i1_oneOf_i49)           |
| [Separator](#modules_items_anyOf_i1_oneOf_i50)           |
| [Shell](#modules_items_anyOf_i1_oneOf_i51)               |
| [Sound](#modules_items_anyOf_i1_oneOf_i52)               |
| [Swap](#modules_items_anyOf_i1_oneOf_i53)                |
| [Terminal](#modules_items_anyOf_i1_oneOf_i54)            |
| [Terminal Font](#modules_items_anyOf_i1_oneOf_i55)       |
| [Terminal Size](#modules_items_anyOf_i1_oneOf_i56)       |
| [Terminal Theme](#modules_items_anyOf_i1_oneOf_i57)      |
| [Theme](#modules_items_anyOf_i1_oneOf_i58)               |
| [Title](#modules_items_anyOf_i1_oneOf_i59)               |
| [TPM](#modules_items_anyOf_i1_oneOf_i60)                 |
| [Users](#modules_items_anyOf_i1_oneOf_i61)               |
| [Uptime](#modules_items_anyOf_i1_oneOf_i62)              |
| [Version](#modules_items_anyOf_i1_oneOf_i63)             |
| [Vulkan](#modules_items_anyOf_i1_oneOf_i64)              |
| [Wallpaper](#modules_items_anyOf_i1_oneOf_i65)           |
| [Weather](#modules_items_anyOf_i1_oneOf_i66)             |
| [Wi-Fi](#modules_items_anyOf_i1_oneOf_i67)               |
| [Window Manager](#modules_items_anyOf_i1_oneOf_i68)      |
| [WM Theme](#modules_items_anyOf_i1_oneOf_i69)            |
| [Zpool](#modules_items_anyOf_i1_oneOf_i70)               |

##### <a name="modules_items_anyOf_i1_oneOf_i0"></a>5.1.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Break`

**Title:** Break

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                         | Pattern | Type  | Deprecated | Definition | Title/Description  |
| ------------------------------------------------ | ------- | ----- | ---------- | ---------- | ------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i0_type ) | No      | const | No         | -          | Print a empty line |

###### <a name="modules_items_anyOf_i1_oneOf_i0_type"></a>5.1.2.1.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Break > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print a empty line

Specific value: `"break"`

##### <a name="modules_items_anyOf_i1_oneOf_i1"></a>5.1.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery`

**Title:** Battery

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition               | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i1_type )               | No      | const            | No         | -                        | Print battery capacity, status, etc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [useSetupApi](#modules_items_anyOf_i1_oneOf_i1_useSetupApi ) | No      | boolean          | No         | -                        | Set if \`SetupAPI\` should be used on Windows to detect battery info, which supports multi batteries, but slower. Windows only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [temp](#modules_items_anyOf_i1_oneOf_i1_temp )               | No      | object           | No         | In #/$defs/temperature   | Detect and display temperature if supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | No      | object           | No         | In #/$defs/percent       | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | No      | string           | No         | In #/$defs/key           | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | No      | enum (of string) | No         | In #/$defs/keyColor      | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | No      | string           | No         | In #/$defs/keyIcon       | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | No      | integer          | No         | In #/$defs/keyWidth      | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | No      | enum (of string) | No         | In #/$defs/outputColor   | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [format](#modules_items_anyOf_i1_oneOf_i1_format )           | No      | string           | No         | In #/$defs/batteryFormat | Output format of the module \`Battery\`. See Wiki for formatting syntax<br />    1. {manufacturer}: Battery manufacturer<br />    2. {model-name}: Battery model name<br />    3. {technology}: Battery technology<br />    4. {capacity}: Battery capacity (percentage num)<br />    5. {status}: Battery status<br />    6. {temperature}: Battery temperature (formatted)<br />    7. {cycle-count}: Battery cycle count<br />    8. {serial}: Battery serial number<br />    9. {manufacture-date}: Battery manufactor date<br />    10. {capacity-bar}: Battery capacity (percentage bar)<br />    11. {time-days}: Battery time remaining days<br />    12. {time-hours}: Battery time remaining hours<br />    13. {time-minutes}: Battery time remaining minutes<br />    14. {time-seconds}: Battery time remaining seconds |

###### <a name="modules_items_anyOf_i1_oneOf_i1_type"></a>5.1.2.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print battery capacity, status, etc

Specific value: `"battery"`

###### <a name="modules_items_anyOf_i1_oneOf_i1_useSetupApi"></a>5.1.2.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > useSetupApi`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if `SetupAPI` should be used on Windows to detect battery info, which supports multi batteries, but slower. Windows only

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp"></a>5.1.2.2.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp`

|                           |                     |
| ------------------------- | ------------------- |
| **Type**                  | `combining`         |
| **Required**              | No                  |
| **Additional properties** | Any type allowed    |
| **Defined in**            | #/$defs/temperature |

**Description:** Detect and display temperature if supported

| One of(Option)                                           |
| -------------------------------------------------------- |
| [item 0](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i0) |
| [item 1](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1) |

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i0"></a>5.1.2.2.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 0`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1"></a>5.1.2.2.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                           | Pattern | Type    | Deprecated | Definition | Title/Description                                                                                                                         |
| ------------------------------------------------------------------ | ------- | ------- | ---------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| - [green](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_green )   | No      | integer | No         | -          | Values (in celsius) less than green will be shown in green                                                                                |
| - [yellow](#modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_yellow ) | No      | integer | No         | -          | Values (in celsius) greater than green and less than yellow will be shown in yellow.<br />Values greater than yellow will be shown in red |

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_green"></a>5.1.2.2.3.2.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > green`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values (in celsius) less than green will be shown in green

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

###### <a name="modules_items_anyOf_i1_oneOf_i1_temp_oneOf_i1_yellow"></a>5.1.2.2.3.2.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > temp > oneOf > item 1 > yellow`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values (in celsius) greater than green and less than yellow will be shown in yellow.
Values greater than yellow will be shown in red

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

###### <a name="modules_items_anyOf_i1_oneOf_i1_percent"></a>5.1.2.2.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent`

|                           |                 |
| ------------------------- | --------------- |
| **Type**                  | `object`        |
| **Required**              | No              |
| **Additional properties** | Not allowed     |
| **Defined in**            | #/$defs/percent |

**Description:** Thresholds for percentage colors

| Property                                                     | Pattern | Type    | Deprecated | Definition                             | Title/Description                                                                                                            |
| ------------------------------------------------------------ | ------- | ------- | ---------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| - [green](#modules_items_anyOf_i1_oneOf_i1_percent_green )   | No      | integer | No         | -                                      | Values less than green will be shown in green                                                                                |
| - [yellow](#modules_items_anyOf_i1_oneOf_i1_percent_yellow ) | No      | integer | No         | -                                      | Values greater than green and less than yellow will be shown in yellow.<br />Values greater than yellow will be shown in red |
| - [type](#modules_items_anyOf_i1_oneOf_i1_percent_type )     | No      | object  | No         | Same as [type](#display_percent_type ) | Set the percentage output type                                                                                               |

###### <a name="modules_items_anyOf_i1_oneOf_i1_percent_green"></a>5.1.2.2.4.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > green`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values less than green will be shown in green

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

###### <a name="modules_items_anyOf_i1_oneOf_i1_percent_yellow"></a>5.1.2.2.4.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > yellow`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Values greater than green and less than yellow will be shown in yellow.
Values greater than yellow will be shown in red

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 100 |

###### <a name="modules_items_anyOf_i1_oneOf_i1_percent_type"></a>5.1.2.2.4.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > percent > type`

|                           |                               |
| ------------------------- | ----------------------------- |
| **Type**                  | `combining`                   |
| **Required**              | No                            |
| **Additional properties** | Any type allowed              |
| **Same definition as**    | [type](#display_percent_type) |

**Description:** Set the percentage output type

###### <a name="modules_items_anyOf_i1_oneOf_i1_key"></a>5.1.2.2.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > key`

|                |             |
| -------------- | ----------- |
| **Type**       | `string`    |
| **Required**   | No          |
| **Defined in** | #/$defs/key |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i1_keyColor"></a>5.1.2.2.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyColor`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Defined in** | #/$defs/keyColor   |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i1_keyIcon"></a>5.1.2.2.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyIcon`

|                |                 |
| -------------- | --------------- |
| **Type**       | `string`        |
| **Required**   | No              |
| **Defined in** | #/$defs/keyIcon |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i1_keyWidth"></a>5.1.2.2.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > keyWidth`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `integer`        |
| **Required**   | No               |
| **Default**    | `0`              |
| **Defined in** | #/$defs/keyWidth |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="modules_items_anyOf_i1_oneOf_i1_outputColor"></a>5.1.2.2.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > outputColor`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `enum (of string)`  |
| **Required**   | No                  |
| **Defined in** | #/$defs/outputColor |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i1_format"></a>5.1.2.2.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Battery > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/batteryFormat |

**Description:** Output format of the module `Battery`. See Wiki for formatting syntax
    1. {manufacturer}: Battery manufacturer
    2. {model-name}: Battery model name
    3. {technology}: Battery technology
    4. {capacity}: Battery capacity (percentage num)
    5. {status}: Battery status
    6. {temperature}: Battery temperature (formatted)
    7. {cycle-count}: Battery cycle count
    8. {serial}: Battery serial number
    9. {manufacture-date}: Battery manufactor date
    10. {capacity-bar}: Battery capacity (percentage bar)
    11. {time-days}: Battery time remaining days
    12. {time-hours}: Battery time remaining hours
    13. {time-minutes}: Battery time remaining minutes
    14. {time-seconds}: Battery time remaining seconds

##### <a name="modules_items_anyOf_i1_oneOf_i2"></a>5.1.2.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS`

**Title:** BIOS

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                              |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i2_type )               | No      | const            | No         | -                                                                    | Print information of 1st-stage bootloader (name, version, release date, etc)                                                                                                                                                                   |
| - [key](#modules_items_anyOf_i1_oneOf_i2_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                              |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i2_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                              |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i2_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                    |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i2_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                     |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i2_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                         |
| - [format](#modules_items_anyOf_i1_oneOf_i2_format )           | No      | string           | No         | In #/$defs/biosFormat                                                | Output format of the module \`Bios\`. See Wiki for formatting syntax<br />    1. {date}: Bios date<br />    2. {release}: Bios release<br />    3. {vendor}: Bios vendor<br />    4. {version}: Bios version<br />    5. {type}: Firmware type |

###### <a name="modules_items_anyOf_i1_oneOf_i2_type"></a>5.1.2.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print information of 1st-stage bootloader (name, version, release date, etc)

Specific value: `"bios"`

###### <a name="modules_items_anyOf_i1_oneOf_i2_key"></a>5.1.2.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i2_keyColor"></a>5.1.2.3.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i2_keyIcon"></a>5.1.2.3.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i2_keyWidth"></a>5.1.2.3.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i2_outputColor"></a>5.1.2.3.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i2_format"></a>5.1.2.3.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BIOS > format`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/biosFormat |

**Description:** Output format of the module `Bios`. See Wiki for formatting syntax
    1. {date}: Bios date
    2. {release}: Bios release
    3. {vendor}: Bios vendor
    4. {version}: Bios version
    5. {type}: Firmware type

##### <a name="modules_items_anyOf_i1_oneOf_i3"></a>5.1.2.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth`

**Title:** Bluetooth

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                 | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------ | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i3_type )                         | No      | const            | No         | -                                                                    | List (connected) bluetooth devices                                                                                                                                                                                                                                                                                        |
| - [showDisconnected](#modules_items_anyOf_i1_oneOf_i3_showDisconnected ) | No      | boolean          | No         | -                                                                    | Set if disconnected bluetooth devices should be printed                                                                                                                                                                                                                                                                   |
| - [percent](#modules_items_anyOf_i1_oneOf_i3_percent )                   | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                          |
| - [key](#modules_items_anyOf_i1_oneOf_i3_key )                           | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                         |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i3_keyColor )                 | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                         |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i3_keyIcon )                   | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                               |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i3_keyWidth )                 | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i3_outputColor )           | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                    |
| - [format](#modules_items_anyOf_i1_oneOf_i3_format )                     | No      | string           | No         | In #/$defs/bluetoothFormat                                           | Output format of the module \`Bluetooth\`. See Wiki for formatting syntax<br />    1. {name}: Name<br />    2. {address}: Address<br />    3. {type}: Type<br />    4. {battery-percentage}: Battery percentage number<br />    5. {connected}: Is connected<br />    6. {battery-percentage-bar}: Battery percentage bar |

###### <a name="modules_items_anyOf_i1_oneOf_i3_type"></a>5.1.2.4.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List (connected) bluetooth devices

Specific value: `"bluetooth"`

###### <a name="modules_items_anyOf_i1_oneOf_i3_showDisconnected"></a>5.1.2.4.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > showDisconnected`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if disconnected bluetooth devices should be printed

###### <a name="modules_items_anyOf_i1_oneOf_i3_percent"></a>5.1.2.4.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i3_key"></a>5.1.2.4.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i3_keyColor"></a>5.1.2.4.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i3_keyIcon"></a>5.1.2.4.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i3_keyWidth"></a>5.1.2.4.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i3_outputColor"></a>5.1.2.4.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i3_format"></a>5.1.2.4.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth > format`

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | No                      |
| **Defined in** | #/$defs/bluetoothFormat |

**Description:** Output format of the module `Bluetooth`. See Wiki for formatting syntax
    1. {name}: Name
    2. {address}: Address
    3. {type}: Type
    4. {battery-percentage}: Battery percentage number
    5. {connected}: Is connected
    6. {battery-percentage-bar}: Battery percentage bar

##### <a name="modules_items_anyOf_i1_oneOf_i4"></a>5.1.2.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio`

**Title:** Bluetooth Radio

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i4_type )               | No      | const            | No         | -                                                                    | List bluetooth radios width supported version and vendor                                                                                                                                                                                                                                                                                                                                                          |
| - [key](#modules_items_anyOf_i1_oneOf_i4_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i4_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                 |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i4_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                       |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i4_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                        |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i4_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                            |
| - [format](#modules_items_anyOf_i1_oneOf_i4_format )           | No      | string           | No         | In #/$defs/bluetoothradioFormat                                      | Output format of the module \`BluetoothRadio\`. See Wiki for formatting syntax<br />    1. {name}: Radio name for discovering<br />    2. {address}: Address<br />    3. {lmp-version}: LMP version<br />    4. {lmp-subversion}: LMP subversion<br />    5. {version}: Bluetooth version<br />    6. {vendor}: Vendor<br />    7. {discoverable}: Discoverable<br />    8. {connectable}: Connectable / Pairable |

###### <a name="modules_items_anyOf_i1_oneOf_i4_type"></a>5.1.2.5.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List bluetooth radios width supported version and vendor

Specific value: `"bluetoothradio"`

###### <a name="modules_items_anyOf_i1_oneOf_i4_key"></a>5.1.2.5.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i4_keyColor"></a>5.1.2.5.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i4_keyIcon"></a>5.1.2.5.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i4_keyWidth"></a>5.1.2.5.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i4_outputColor"></a>5.1.2.5.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i4_format"></a>5.1.2.5.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Bluetooth Radio > format`

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `string`                     |
| **Required**   | No                           |
| **Defined in** | #/$defs/bluetoothradioFormat |

**Description:** Output format of the module `BluetoothRadio`. See Wiki for formatting syntax
    1. {name}: Radio name for discovering
    2. {address}: Address
    3. {lmp-version}: LMP version
    4. {lmp-subversion}: LMP subversion
    5. {version}: Bluetooth version
    6. {vendor}: Vendor
    7. {discoverable}: Discoverable
    8. {connectable}: Connectable / Pairable

##### <a name="modules_items_anyOf_i1_oneOf_i5"></a>5.1.2.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board`

**Title:** Board

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                      |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i5_type )               | No      | const            | No         | -                                                                    | Print motherboard name and other info                                                                                                                                                                                  |
| - [key](#modules_items_anyOf_i1_oneOf_i5_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i5_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i5_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i5_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i5_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i5_format )           | No      | string           | No         | In #/$defs/boardFormat                                               | Output format of the module \`Board\`. See Wiki for formatting syntax<br />    1. {name}: Board name<br />    2. {vendor}: Board vendor<br />    3. {version}: Board version<br />    4. {serial}: Board serial number |

###### <a name="modules_items_anyOf_i1_oneOf_i5_type"></a>5.1.2.6.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print motherboard name and other info

Specific value: `"board"`

###### <a name="modules_items_anyOf_i1_oneOf_i5_key"></a>5.1.2.6.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i5_keyColor"></a>5.1.2.6.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i5_keyIcon"></a>5.1.2.6.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i5_keyWidth"></a>5.1.2.6.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i5_outputColor"></a>5.1.2.6.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i5_format"></a>5.1.2.6.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Board > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/boardFormat |

**Description:** Output format of the module `Board`. See Wiki for formatting syntax
    1. {name}: Board name
    2. {vendor}: Board vendor
    3. {version}: Board version
    4. {serial}: Board serial number

##### <a name="modules_items_anyOf_i1_oneOf_i6"></a>5.1.2.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager`

**Title:** Boot Manager

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i6_type )               | No      | const            | No         | -                                                                    | Print information of 2nd-stage bootloader (name, firmware, etc)                                                                                                                                                                                                                                  |
| - [key](#modules_items_anyOf_i1_oneOf_i6_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i6_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i6_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                      |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i6_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                       |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i6_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                           |
| - [format](#modules_items_anyOf_i1_oneOf_i6_format )           | No      | string           | No         | In #/$defs/bootmgrFormat                                             | Output format of the module \`Bootmgr\`. See Wiki for formatting syntax<br />    1. {name}: Name / description<br />    2. {firmware-path}: Firmware file path<br />    3. {firmware-name}: Firmware file name<br />    4. {secure-boot}: Is secure boot enabled<br />    5. {order}: Boot order |

###### <a name="modules_items_anyOf_i1_oneOf_i6_type"></a>5.1.2.7.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print information of 2nd-stage bootloader (name, firmware, etc)

Specific value: `"bootmgr"`

###### <a name="modules_items_anyOf_i1_oneOf_i6_key"></a>5.1.2.7.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i6_keyColor"></a>5.1.2.7.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i6_keyIcon"></a>5.1.2.7.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i6_keyWidth"></a>5.1.2.7.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i6_outputColor"></a>5.1.2.7.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i6_format"></a>5.1.2.7.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Boot Manager > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/bootmgrFormat |

**Description:** Output format of the module `Bootmgr`. See Wiki for formatting syntax
    1. {name}: Name / description
    2. {firmware-path}: Firmware file path
    3. {firmware-name}: Firmware file name
    4. {secure-boot}: Is secure boot enabled
    5. {order}: Boot order

##### <a name="modules_items_anyOf_i1_oneOf_i7"></a>5.1.2.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness`

**Title:** Brightness

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i7_type )               | No      | const            | No         | -                                                                    | Print current brightness level of your monitors                                                                                                                                                                                                                                                                                                                                                                               |
| - [percent](#modules_items_anyOf_i1_oneOf_i7_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                              |
| - [ddcciSleep](#modules_items_anyOf_i1_oneOf_i7_ddcciSleep )   | No      | integer          | No         | -                                                                    | Set the sleep times (in ms) when sending DDC/CI requests.<br />See <https://www.ddcutil.com/performance_options/#option-sleep-multiplier> for detail                                                                                                                                                                                                                                                                          |
| - [compact](#modules_items_anyOf_i1_oneOf_i7_compact )         | No      | boolean          | No         | -                                                                    | Set if multiple results should be printed in one line                                                                                                                                                                                                                                                                                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i7_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i7_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                             |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i7_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i7_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                    |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i7_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                        |
| - [format](#modules_items_anyOf_i1_oneOf_i7_format )           | No      | string           | No         | In #/$defs/brightnessFormat                                          | Output format of the module \`Brightness\`. See Wiki for formatting syntax<br />    1. {percentage}: Screen brightness (percentage num)<br />    2. {name}: Screen name<br />    3. {max}: Maximum brightness value<br />    4. {min}: Minimum brightness value<br />    5. {current}: Current brightness value<br />    6. {percentage-bar}: Screen brightness (percentage bar)<br />    7. {is-builtin}: Is built-in screen |

###### <a name="modules_items_anyOf_i1_oneOf_i7_type"></a>5.1.2.8.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current brightness level of your monitors

Specific value: `"brightness"`

###### <a name="modules_items_anyOf_i1_oneOf_i7_percent"></a>5.1.2.8.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i7_ddcciSleep"></a>5.1.2.8.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > ddcciSleep`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `10`      |

**Description:** Set the sleep times (in ms) when sending DDC/CI requests.
See <https://www.ddcutil.com/performance_options/#option-sleep-multiplier> for detail

| Restrictions |          |
| ------------ | -------- |
| **Minimum**  | &ge; 0   |
| **Maximum**  | &le; 400 |

###### <a name="modules_items_anyOf_i1_oneOf_i7_compact"></a>5.1.2.8.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > compact`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if multiple results should be printed in one line

###### <a name="modules_items_anyOf_i1_oneOf_i7_key"></a>5.1.2.8.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i7_keyColor"></a>5.1.2.8.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i7_keyIcon"></a>5.1.2.8.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i7_keyWidth"></a>5.1.2.8.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i7_outputColor"></a>5.1.2.8.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i7_format"></a>5.1.2.8.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Brightness > format`

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `string`                 |
| **Required**   | No                       |
| **Defined in** | #/$defs/brightnessFormat |

**Description:** Output format of the module `Brightness`. See Wiki for formatting syntax
    1. {percentage}: Screen brightness (percentage num)
    2. {name}: Screen name
    3. {max}: Maximum brightness value
    4. {min}: Minimum brightness value
    5. {current}: Current brightness value
    6. {percentage-bar}: Screen brightness (percentage bar)
    7. {is-builtin}: Is built-in screen

##### <a name="modules_items_anyOf_i1_oneOf_i8"></a>5.1.2.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS`

**Title:** BTRFS

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i8_type )               | No      | const            | No         | -                                                                    | Print Linux BTRFS volumes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [percent](#modules_items_anyOf_i1_oneOf_i8_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [key](#modules_items_anyOf_i1_oneOf_i8_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i8_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i8_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i8_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i8_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [format](#modules_items_anyOf_i1_oneOf_i8_format )           | No      | string           | No         | In #/$defs/btrfsFormat                                               | Output format of the module \`Btrfs\`. See Wiki for formatting syntax<br />    1. {name}: Name / Label<br />    2. {uuid}: UUID<br />    3. {devices}: Associated devices<br />    4. {features}: Enabled features<br />    5. {used}: Size used<br />    6. {allocated}: Size allocated<br />    7. {total}: Size total<br />    8. {used-percentage}: Used percentage num<br />    9. {allocated-percentage}: Allocated percentage num<br />    10. {used-percentage-bar}: Used percentage bar<br />    11. {allocated-percentage-bar}: Allocated percentage bar<br />    12. {node-size}: Node size<br />    13. {sector-size}: Sector size |

###### <a name="modules_items_anyOf_i1_oneOf_i8_type"></a>5.1.2.9.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print Linux BTRFS volumes

Specific value: `"btrfs"`

###### <a name="modules_items_anyOf_i1_oneOf_i8_percent"></a>5.1.2.9.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i8_key"></a>5.1.2.9.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i8_keyColor"></a>5.1.2.9.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i8_keyIcon"></a>5.1.2.9.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i8_keyWidth"></a>5.1.2.9.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i8_outputColor"></a>5.1.2.9.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i8_format"></a>5.1.2.9.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > BTRFS > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/btrfsFormat |

**Description:** Output format of the module `Btrfs`. See Wiki for formatting syntax
    1. {name}: Name / Label
    2. {uuid}: UUID
    3. {devices}: Associated devices
    4. {features}: Enabled features
    5. {used}: Size used
    6. {allocated}: Size allocated
    7. {total}: Size total
    8. {used-percentage}: Used percentage num
    9. {allocated-percentage}: Allocated percentage num
    10. {used-percentage-bar}: Used percentage bar
    11. {allocated-percentage-bar}: Allocated percentage bar
    12. {node-size}: Node size
    13. {sector-size}: Sector size

##### <a name="modules_items_anyOf_i1_oneOf_i9"></a>5.1.2.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera`

**Title:** Camera

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                       | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i9_type )               | No      | const            | No         | -                                                                    | Print available cameras                                                                                                                                                                                                                                                        |
| - [key](#modules_items_anyOf_i1_oneOf_i9_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                              |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i9_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                              |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i9_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                    |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i9_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                     |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i9_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                         |
| - [format](#modules_items_anyOf_i1_oneOf_i9_format )           | No      | string           | No         | In #/$defs/cameraFormat                                              | Output format of the module \`Camera\`. See Wiki for formatting syntax<br />    1. {name}: Device name<br />    2. {vendor}: Vendor<br />    3. {colorspace}: Color space<br />    4. {id}: Identifier<br />    5. {width}: Width (in px)<br />    6. {height}: Height (in px) |

###### <a name="modules_items_anyOf_i1_oneOf_i9_type"></a>5.1.2.10.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print available cameras

Specific value: `"camera"`

###### <a name="modules_items_anyOf_i1_oneOf_i9_key"></a>5.1.2.10.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i9_keyColor"></a>5.1.2.10.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i9_keyIcon"></a>5.1.2.10.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i9_keyWidth"></a>5.1.2.10.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i9_outputColor"></a>5.1.2.10.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i9_format"></a>5.1.2.10.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Camera > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/cameraFormat |

**Description:** Output format of the module `Camera`. See Wiki for formatting syntax
    1. {name}: Device name
    2. {vendor}: Vendor
    3. {colorspace}: Color space
    4. {id}: Identifier
    5. {width}: Width (in px)
    6. {height}: Height (in px)

##### <a name="modules_items_anyOf_i1_oneOf_i10"></a>5.1.2.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis`

**Title:** Chassis

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i10_type )               | No      | const            | No         | -                                                                    | Print chassis type (desktop, laptop, etc)                                                                                                                                                                                        |
| - [key](#modules_items_anyOf_i1_oneOf_i10_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i10_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i10_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                      |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i10_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                       |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i10_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                           |
| - [format](#modules_items_anyOf_i1_oneOf_i10_format )           | No      | string           | No         | In #/$defs/chassisFormat                                             | Output format of the module \`Chassis\`. See Wiki for formatting syntax<br />    1. {type}: Chassis type<br />    2. {vendor}: Chassis vendor<br />    3. {version}: Chassis version<br />    4. {serial}: Chassis serial number |

###### <a name="modules_items_anyOf_i1_oneOf_i10_type"></a>5.1.2.11.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print chassis type (desktop, laptop, etc)

Specific value: `"chassis"`

###### <a name="modules_items_anyOf_i1_oneOf_i10_key"></a>5.1.2.11.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i10_keyColor"></a>5.1.2.11.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i10_keyIcon"></a>5.1.2.11.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i10_keyWidth"></a>5.1.2.11.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i10_outputColor"></a>5.1.2.11.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i10_format"></a>5.1.2.11.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Chassis > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/chassisFormat |

**Description:** Output format of the module `Chassis`. See Wiki for formatting syntax
    1. {type}: Chassis type
    2. {vendor}: Chassis vendor
    3. {version}: Chassis version
    4. {serial}: Chassis serial number

##### <a name="modules_items_anyOf_i1_oneOf_i11"></a>5.1.2.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU`

**Title:** CPU

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i11_type )                       | No      | const            | No         | -                                                                    | Print CPU name, frequency, etc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [temp](#modules_items_anyOf_i1_oneOf_i11_temp )                       | No      | object           | No         | Same as [temp](#modules_items_anyOf_i1_oneOf_i1_temp )               | Detect and display temperature if supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [showPeCoreCount](#modules_items_anyOf_i1_oneOf_i11_showPeCoreCount ) | No      | boolean          | No         | -                                                                    | Detect and display CPU frequency of different core types (eg. Pcore and Ecore) if supported                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [key](#modules_items_anyOf_i1_oneOf_i11_key )                         | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i11_keyColor )               | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i11_keyIcon )                 | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i11_keyWidth )               | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i11_outputColor )         | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [format](#modules_items_anyOf_i1_oneOf_i11_format )                   | No      | string           | No         | In #/$defs/cpuFormat                                                 | Output format of the module \`CPU\`. See Wiki for formatting syntax<br />    1. {name}: Name<br />    2. {vendor}: Vendor<br />    3. {cores-physical}: Physical core count<br />    4. {cores-logical}: Logical core count<br />    5. {cores-online}: Online core count<br />    6. {freq-base}: Base frequency (formatted)<br />    7. {freq-max}: Max frequency (formatted)<br />    8. {temperature}: Temperature (formatted)<br />    9. {core-types}: Logical core count grouped by frequency<br />    10. {packages}: Processor package count |

###### <a name="modules_items_anyOf_i1_oneOf_i11_type"></a>5.1.2.12.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print CPU name, frequency, etc

Specific value: `"cpu"`

###### <a name="modules_items_anyOf_i1_oneOf_i11_temp"></a>5.1.2.12.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > temp`

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [temp](#modules_items_anyOf_i1_oneOf_i1_temp) |

**Description:** Detect and display temperature if supported

###### <a name="modules_items_anyOf_i1_oneOf_i11_showPeCoreCount"></a>5.1.2.12.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > showPeCoreCount`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Detect and display CPU frequency of different core types (eg. Pcore and Ecore) if supported

###### <a name="modules_items_anyOf_i1_oneOf_i11_key"></a>5.1.2.12.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i11_keyColor"></a>5.1.2.12.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i11_keyIcon"></a>5.1.2.12.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i11_keyWidth"></a>5.1.2.12.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i11_outputColor"></a>5.1.2.12.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i11_format"></a>5.1.2.12.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU > format`

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/cpuFormat |

**Description:** Output format of the module `CPU`. See Wiki for formatting syntax
    1. {name}: Name
    2. {vendor}: Vendor
    3. {cores-physical}: Physical core count
    4. {cores-logical}: Logical core count
    5. {cores-online}: Online core count
    6. {freq-base}: Base frequency (formatted)
    7. {freq-max}: Max frequency (formatted)
    8. {temperature}: Temperature (formatted)
    9. {core-types}: Logical core count grouped by frequency
    10. {packages}: Processor package count

##### <a name="modules_items_anyOf_i1_oneOf_i12"></a>5.1.2.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache`

**Title:** CPU Cache

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                            |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i12_type )               | No      | const            | No         | -                                                                    | Print CPU cache sizes                                                                                                                        |
| - [percent](#modules_items_anyOf_i1_oneOf_i12_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                             |
| - [key](#modules_items_anyOf_i1_oneOf_i12_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                            |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i12_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                            |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i12_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                  |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i12_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                   |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i12_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                       |
| - [format](#modules_items_anyOf_i1_oneOf_i12_format )           | No      | string           | No         | In #/$defs/cpucacheFormat                                            | Output format of the module \`CPUCache\`. See Wiki for formatting syntax<br />    1. {result}: Separate result<br />    2. {sum}: Sum result |

###### <a name="modules_items_anyOf_i1_oneOf_i12_type"></a>5.1.2.13.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print CPU cache sizes

Specific value: `"cpucache"`

###### <a name="modules_items_anyOf_i1_oneOf_i12_percent"></a>5.1.2.13.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i12_key"></a>5.1.2.13.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i12_keyColor"></a>5.1.2.13.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i12_keyIcon"></a>5.1.2.13.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i12_keyWidth"></a>5.1.2.13.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i12_outputColor"></a>5.1.2.13.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i12_format"></a>5.1.2.13.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Cache > format`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/cpucacheFormat |

**Description:** Output format of the module `CPUCache`. See Wiki for formatting syntax
    1. {result}: Separate result
    2. {sum}: Sum result

##### <a name="modules_items_anyOf_i1_oneOf_i13"></a>5.1.2.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage`

**Title:** CPU Usage

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i13_type )               | No      | const            | No         | -                                                                    | Print CPU usage. Costs some time to collect data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [percent](#modules_items_anyOf_i1_oneOf_i13_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [separate](#modules_items_anyOf_i1_oneOf_i13_separate )       | No      | boolean          | No         | -                                                                    | Display CPU usage per CPU logical core, instead of an average result                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [waitTime](#modules_items_anyOf_i1_oneOf_i13_waitTime )       | No      | integer          | No         | -                                                                    | Wait time (in ms). CPU usage = (inUseEnd - inUseStart) / waitTime                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [key](#modules_items_anyOf_i1_oneOf_i13_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i13_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i13_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i13_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i13_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [format](#modules_items_anyOf_i1_oneOf_i13_format )           | No      | string           | No         | In #/$defs/cpuusageFormat                                            | Output format of the module \`CPUUsage\`. See Wiki for formatting syntax<br />    1. {avg}: CPU usage (percentage num, average)<br />    2. {max}: CPU usage (percentage num, maximum)<br />    3. {max-index}: CPU core index of maximum usage<br />    4. {min}: CPU usage (percentage num, minimum)<br />    5. {min-index}: CPU core index of minimum usage<br />    6. {avg-bar}: CPU usage (percentage bar, average)<br />    7. {max-bar}: CPU usage (percentage bar, maximum)<br />    8. {min-bar}: CPU usage (percentage bar, minimum) |

###### <a name="modules_items_anyOf_i1_oneOf_i13_type"></a>5.1.2.14.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print CPU usage. Costs some time to collect data

Specific value: `"cpuusage"`

###### <a name="modules_items_anyOf_i1_oneOf_i13_percent"></a>5.1.2.14.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i13_separate"></a>5.1.2.14.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > separate`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Display CPU usage per CPU logical core, instead of an average result

###### <a name="modules_items_anyOf_i1_oneOf_i13_waitTime"></a>5.1.2.14.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > waitTime`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Wait time (in ms). CPU usage = (inUseEnd - inUseStart) / waitTime

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

###### <a name="modules_items_anyOf_i1_oneOf_i13_key"></a>5.1.2.14.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i13_keyColor"></a>5.1.2.14.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i13_keyIcon"></a>5.1.2.14.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i13_keyWidth"></a>5.1.2.14.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i13_outputColor"></a>5.1.2.14.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i13_format"></a>5.1.2.14.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > CPU Usage > format`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/cpuusageFormat |

**Description:** Output format of the module `CPUUsage`. See Wiki for formatting syntax
    1. {avg}: CPU usage (percentage num, average)
    2. {max}: CPU usage (percentage num, maximum)
    3. {max-index}: CPU core index of maximum usage
    4. {min}: CPU usage (percentage num, minimum)
    5. {min-index}: CPU core index of minimum usage
    6. {avg-bar}: CPU usage (percentage bar, average)
    7. {max-bar}: CPU usage (percentage bar, maximum)
    8. {min-bar}: CPU usage (percentage bar, minimum)

##### <a name="modules_items_anyOf_i1_oneOf_i14"></a>5.1.2.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors`

**Title:** Colors

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                   | Title/Description                                           |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i14_type )               | No      | const            | No         | -                                                            | Print some colored blocks                                   |
| - [symbol](#modules_items_anyOf_i1_oneOf_i14_symbol )           | No      | enum (of string) | No         | -                                                            | Set the symbol to use                                       |
| - [paddingLeft](#modules_items_anyOf_i1_oneOf_i14_paddingLeft ) | No      | integer          | No         | -                                                            | Set the number of white spaces to print before the symbol   |
| - [block](#modules_items_anyOf_i1_oneOf_i14_block )             | No      | object           | No         | -                                                            | Set behavior of block printing                              |
| - [key](#modules_items_anyOf_i1_oneOf_i14_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )         | Key of the module                                           |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i14_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon ) | Set the icon to be displayed by \`display.keyType: "icon"\` |

###### <a name="modules_items_anyOf_i1_oneOf_i14_type"></a>5.1.2.15.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print some colored blocks

Specific value: `"colors"`

###### <a name="modules_items_anyOf_i1_oneOf_i14_symbol"></a>5.1.2.15.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > symbol`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"background"`     |

**Description:** Set the symbol to use

Must be one of:
* "block"
* "background"
* "circle"
* "diamond"
* "triangle"
* "square"
* "star"

###### <a name="modules_items_anyOf_i1_oneOf_i14_paddingLeft"></a>5.1.2.15.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > paddingLeft`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Set the number of white spaces to print before the symbol

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="modules_items_anyOf_i1_oneOf_i14_block"></a>5.1.2.15.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set behavior of block printing

| Property                                                  | Pattern | Type             | Deprecated | Definition | Title/Description                              |
| --------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------------------------------- |
| - [width](#modules_items_anyOf_i1_oneOf_i14_block_width ) | No      | integer          | No         | -          | Set the block width in spaces                  |
| - [range](#modules_items_anyOf_i1_oneOf_i14_block_range ) | No      | array of integer | No         | -          | Set the range of colors in the blocks to print |

###### <a name="modules_items_anyOf_i1_oneOf_i14_block_width"></a>5.1.2.15.4.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > width`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `3`       |

**Description:** Set the block width in spaces

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

###### <a name="modules_items_anyOf_i1_oneOf_i14_block_range"></a>5.1.2.15.4.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `array of integer` |
| **Required** | No                 |

**Description:** Set the range of colors in the blocks to print

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 2                  |
| **Max items**        | 2                  |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [range items](#modules_items_anyOf_i1_oneOf_i14_block_range_items) | -           |

###### <a name="modules_items_anyOf_i1_oneOf_i14_block_range_items"></a>5.1.2.15.4.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > block > range > range items

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

| Restrictions |         |
| ------------ | ------- |
| **Minimum**  | &ge; 0  |
| **Maximum**  | &le; 15 |

###### <a name="modules_items_anyOf_i1_oneOf_i14_key"></a>5.1.2.15.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i14_keyIcon"></a>5.1.2.15.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Colors > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

##### <a name="modules_items_anyOf_i1_oneOf_i15"></a>5.1.2.16. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command`

**Title:** Command

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                            |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i15_type )               | No      | const            | No         | -                                                                    | Running custom shell scripts                                                                                 |
| - [shell](#modules_items_anyOf_i1_oneOf_i15_shell )             | No      | string           | No         | -                                                                    | Set the shell program to execute the command text<br />Default: cmd for Windows, /bin/sh for *nix            |
| - [param](#modules_items_anyOf_i1_oneOf_i15_param )             | No      | string           | No         | -                                                                    | Set the parameter used when starting the shell<br />Default: /c for Windows, -c for *nix                     |
| - [text](#modules_items_anyOf_i1_oneOf_i15_text )               | No      | string           | No         | -                                                                    | Set the command text to be executed                                                                          |
| - [key](#modules_items_anyOf_i1_oneOf_i15_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                            |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i15_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                            |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i15_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                  |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i15_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                   |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i15_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                       |
| - [format](#modules_items_anyOf_i1_oneOf_i15_format )           | No      | string           | No         | In #/$defs/commandFormat                                             | Output format of the module \`Command\`. See Wiki for formatting syntax<br />    1. {result}: Command result |

###### <a name="modules_items_anyOf_i1_oneOf_i15_type"></a>5.1.2.16.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Running custom shell scripts

Specific value: `"command"`

###### <a name="modules_items_anyOf_i1_oneOf_i15_shell"></a>5.1.2.16.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > shell`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the shell program to execute the command text
Default: cmd for Windows, /bin/sh for *nix

###### <a name="modules_items_anyOf_i1_oneOf_i15_param"></a>5.1.2.16.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > param`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the parameter used when starting the shell
Default: /c for Windows, -c for *nix

###### <a name="modules_items_anyOf_i1_oneOf_i15_text"></a>5.1.2.16.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > text`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Set the command text to be executed

###### <a name="modules_items_anyOf_i1_oneOf_i15_key"></a>5.1.2.16.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i15_keyColor"></a>5.1.2.16.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i15_keyIcon"></a>5.1.2.16.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i15_keyWidth"></a>5.1.2.16.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i15_outputColor"></a>5.1.2.16.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i15_format"></a>5.1.2.16.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Command > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/commandFormat |

**Description:** Output format of the module `Command`. See Wiki for formatting syntax
    1. {result}: Command result

##### <a name="modules_items_anyOf_i1_oneOf_i16"></a>5.1.2.17. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor`

**Title:** Cursor

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                        |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i16_type )               | No      | const            | No         | -                                                                    | Print cursor style name                                                                                                                  |
| - [percent](#modules_items_anyOf_i1_oneOf_i16_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i16_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i16_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i16_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i16_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i16_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i16_format )           | No      | string           | No         | In #/$defs/cursorFormat                                              | Output format of the module \`Cursor\`. See Wiki for formatting syntax<br />    1. {theme}: Cursor theme<br />    2. {size}: Cursor size |

###### <a name="modules_items_anyOf_i1_oneOf_i16_type"></a>5.1.2.17.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print cursor style name

Specific value: `"cursor"`

###### <a name="modules_items_anyOf_i1_oneOf_i16_percent"></a>5.1.2.17.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i16_key"></a>5.1.2.17.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i16_keyColor"></a>5.1.2.17.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i16_keyIcon"></a>5.1.2.17.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i16_keyWidth"></a>5.1.2.17.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i16_outputColor"></a>5.1.2.17.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i16_format"></a>5.1.2.17.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Cursor > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/cursorFormat |

**Description:** Output format of the module `Cursor`. See Wiki for formatting syntax
    1. {theme}: Cursor theme
    2. {size}: Cursor size

##### <a name="modules_items_anyOf_i1_oneOf_i17"></a>5.1.2.18. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom`

**Title:** Custom

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i17_type )               | No      | const            | No         | -                                                                    | Print a custom string, with or without key                             |
| - [key](#modules_items_anyOf_i1_oneOf_i17_key )                 | No      | string           | No         | -                                                                    | Leave empty not to print the key                                       |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i17_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i17_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i17_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i17_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\` |
| - [format](#modules_items_anyOf_i1_oneOf_i17_format )           | No      | string           | No         | -                                                                    | Text to print                                                          |

###### <a name="modules_items_anyOf_i1_oneOf_i17_type"></a>5.1.2.18.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print a custom string, with or without key

Specific value: `"custom"`

###### <a name="modules_items_anyOf_i1_oneOf_i17_key"></a>5.1.2.18.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > key`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Leave empty not to print the key

###### <a name="modules_items_anyOf_i1_oneOf_i17_keyColor"></a>5.1.2.18.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i17_keyIcon"></a>5.1.2.18.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i17_keyWidth"></a>5.1.2.18.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i17_outputColor"></a>5.1.2.18.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i17_format"></a>5.1.2.18.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Custom > format`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Text to print

##### <a name="modules_items_anyOf_i1_oneOf_i18"></a>5.1.2.19. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time`

**Title:** Date Time

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i18_type )               | No      | const            | No         | -                                                                    | Print current date and time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [percent](#modules_items_anyOf_i1_oneOf_i18_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [key](#modules_items_anyOf_i1_oneOf_i18_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i18_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i18_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i18_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i18_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i18_format )           | No      | string           | No         | In #/$defs/datetimeFormat                                            | Output format of the module \`DateTime\`. See Wiki for formatting syntax<br />    1. {year}: Year<br />    2. {year-short}: Last two digits of year<br />    3. {month}: Month<br />    4. {month-pretty}: Month with leading zero<br />    5. {month-name}: Month name<br />    6. {month-name-short}: Month name short<br />    7. {week}: Week number on year<br />    8. {weekday}: Weekday<br />    9. {weekday-short}: Weekday short<br />    10. {day-in-year}: Day in year<br />    11. {day-in-month}: Day in month<br />    12. {day-in-week}: Day in week<br />    13. {hour}: Hour<br />    14. {hour-pretty}: Hour with leading zero<br />    15. {hour-12}: Hour 12h format<br />    16. {hour-12-pretty}: Hour 12h format with leading zero<br />    17. {minute}: Minute<br />    18. {minute-pretty}: Minute with leading zero<br />    19. {second}: Second<br />    20. {second-pretty}: Second with leading zero<br />    21. {offset-from-utc}: Offset from UTC in the ISO 8601 format<br />    22. {timezone-name}: Locale-dependent timezone name or abbreviation<br />    23. {day-pretty}: Day in month with leading zero |

###### <a name="modules_items_anyOf_i1_oneOf_i18_type"></a>5.1.2.19.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current date and time

Specific value: `"datetime"`

###### <a name="modules_items_anyOf_i1_oneOf_i18_percent"></a>5.1.2.19.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i18_key"></a>5.1.2.19.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i18_keyColor"></a>5.1.2.19.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i18_keyIcon"></a>5.1.2.19.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i18_keyWidth"></a>5.1.2.19.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i18_outputColor"></a>5.1.2.19.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i18_format"></a>5.1.2.19.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Date Time > format`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/datetimeFormat |

**Description:** Output format of the module `DateTime`. See Wiki for formatting syntax
    1. {year}: Year
    2. {year-short}: Last two digits of year
    3. {month}: Month
    4. {month-pretty}: Month with leading zero
    5. {month-name}: Month name
    6. {month-name-short}: Month name short
    7. {week}: Week number on year
    8. {weekday}: Weekday
    9. {weekday-short}: Weekday short
    10. {day-in-year}: Day in year
    11. {day-in-month}: Day in month
    12. {day-in-week}: Day in week
    13. {hour}: Hour
    14. {hour-pretty}: Hour with leading zero
    15. {hour-12}: Hour 12h format
    16. {hour-12-pretty}: Hour 12h format with leading zero
    17. {minute}: Minute
    18. {minute-pretty}: Minute with leading zero
    19. {second}: Second
    20. {second-pretty}: Second with leading zero
    21. {offset-from-utc}: Offset from UTC in the ISO 8601 format
    22. {timezone-name}: Locale-dependent timezone name or abbreviation
    23. {day-pretty}: Day in month with leading zero

##### <a name="modules_items_anyOf_i1_oneOf_i19"></a>5.1.2.20. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display`

**Title:** Display

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                      | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i19_type )                             | No      | const            | No         | -                                                                    | Print resolutions, refresh rates, etc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [compactType](#modules_items_anyOf_i1_oneOf_i19_compactType )               | No      | enum (of string) | No         | -                                                                    | Set if all displays should be printed in one line                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [preciseRefreshRate](#modules_items_anyOf_i1_oneOf_i19_preciseRefreshRate ) | No      | boolean          | No         | -                                                                    | Set if decimal refresh rates should not be rounded into integers when printing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [order](#modules_items_anyOf_i1_oneOf_i19_order )                           | No      | enum (of string) | No         | -                                                                    | Set the order should be used when printing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [key](#modules_items_anyOf_i1_oneOf_i19_key )                               | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i19_keyColor )                     | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i19_keyIcon )                       | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i19_keyWidth )                     | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i19_outputColor )               | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i19_format )                         | No      | string           | No         | In #/$defs/displayFormat                                             | Output format of the module \`Display\`. See Wiki for formatting syntax<br />    1. {width}: Screen configured width (in pixels)<br />    2. {height}: Screen configured height (in pixels)<br />    3. {refresh-rate}: Screen configured refresh rate (in Hz)<br />    4. {scaled-width}: Screen scaled width (in pixels)<br />    5. {scaled-height}: Screen scaled height (in pixels)<br />    6. {name}: Screen name<br />    7. {type}: Screen type (Built-in or External)<br />    8. {rotation}: Screen rotation (in degrees)<br />    9. {is-primary}: True if being the primary screen<br />    10. {physical-width}: Screen physical width (in millimeters)<br />    11. {physical-height}: Screen physical height (in millimeters)<br />    12. {inch}: Physical diagonal length in inches<br />    13. {ppi}: Pixels per inch (PPI)<br />    14. {bit-depth}: Bits per color channel<br />    15. {hdr-enabled}: True if high dynamic range (HDR) mode is enabled<br />    16. {manufacture-year}: Year of manufacturing<br />    17. {manufacture-week}: Nth week of manufacturing in the year<br />    18. {serial}: Serial number<br />    19. {platform-api}: The platform API used when detecting the display<br />    20. {hdr-compatible}: True if the display is HDR compatible<br />    21. {scale-factor}: HiDPI scale factor<br />    22. {preferred-width}: Screen preferred width (in pixels)<br />    23. {preferred-height}: Screen preferred height (in pixels)<br />    24. {preferred-refresh-rate}: Screen preferred refresh rate (in Hz) |

###### <a name="modules_items_anyOf_i1_oneOf_i19_type"></a>5.1.2.20.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print resolutions, refresh rates, etc

Specific value: `"display"`

###### <a name="modules_items_anyOf_i1_oneOf_i19_compactType"></a>5.1.2.20.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > compactType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"none"`           |

**Description:** Set if all displays should be printed in one line

Must be one of:
* "none"
* "original"
* "scaled"
* "original-with-refresh-rate"
* "scaled-with-refresh-rate"

###### <a name="modules_items_anyOf_i1_oneOf_i19_preciseRefreshRate"></a>5.1.2.20.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > preciseRefreshRate`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if decimal refresh rates should not be rounded into integers when printing

###### <a name="modules_items_anyOf_i1_oneOf_i19_order"></a>5.1.2.20.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > order`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"none"`           |

**Description:** Set the order should be used when printing

Must be one of:
* "none"
* "asc"
* "desc"

###### <a name="modules_items_anyOf_i1_oneOf_i19_key"></a>5.1.2.20.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i19_keyColor"></a>5.1.2.20.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i19_keyIcon"></a>5.1.2.20.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i19_keyWidth"></a>5.1.2.20.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i19_outputColor"></a>5.1.2.20.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i19_format"></a>5.1.2.20.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Display > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/displayFormat |

**Description:** Output format of the module `Display`. See Wiki for formatting syntax
    1. {width}: Screen configured width (in pixels)
    2. {height}: Screen configured height (in pixels)
    3. {refresh-rate}: Screen configured refresh rate (in Hz)
    4. {scaled-width}: Screen scaled width (in pixels)
    5. {scaled-height}: Screen scaled height (in pixels)
    6. {name}: Screen name
    7. {type}: Screen type (Built-in or External)
    8. {rotation}: Screen rotation (in degrees)
    9. {is-primary}: True if being the primary screen
    10. {physical-width}: Screen physical width (in millimeters)
    11. {physical-height}: Screen physical height (in millimeters)
    12. {inch}: Physical diagonal length in inches
    13. {ppi}: Pixels per inch (PPI)
    14. {bit-depth}: Bits per color channel
    15. {hdr-enabled}: True if high dynamic range (HDR) mode is enabled
    16. {manufacture-year}: Year of manufacturing
    17. {manufacture-week}: Nth week of manufacturing in the year
    18. {serial}: Serial number
    19. {platform-api}: The platform API used when detecting the display
    20. {hdr-compatible}: True if the display is HDR compatible
    21. {scale-factor}: HiDPI scale factor
    22. {preferred-width}: Screen preferred width (in pixels)
    23. {preferred-height}: Screen preferred height (in pixels)
    24. {preferred-refresh-rate}: Screen preferred refresh rate (in Hz)

##### <a name="modules_items_anyOf_i1_oneOf_i20"></a>5.1.2.21. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk`

**Title:** Disk

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                              | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i20_type )                     | No      | const            | No         | -                                                                    | Print partitions, space usage, disk type, etc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [folders](#modules_items_anyOf_i1_oneOf_i20_folders )               | No      | string           | No         | -                                                                    | A colon (semicolon on Windows) separated list of folder paths for the disk output<br />Default: auto detection using mount-points<br />This option overrides other \`show*\` options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [showExternal](#modules_items_anyOf_i1_oneOf_i20_showExternal )     | No      | boolean          | No         | -                                                                    | Set if external volume should be printed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [showHidden](#modules_items_anyOf_i1_oneOf_i20_showHidden )         | No      | boolean          | No         | -                                                                    | Set if hidden volumes should be printed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [showSubvolumes](#modules_items_anyOf_i1_oneOf_i20_showSubvolumes ) | No      | boolean          | No         | -                                                                    | Set if subvolumes should be printed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [showReadOnly](#modules_items_anyOf_i1_oneOf_i20_showReadOnly )     | No      | boolean          | No         | -                                                                    | Set if read only volumes should be printed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [showUnknown](#modules_items_anyOf_i1_oneOf_i20_showUnknown )       | No      | boolean          | No         | -                                                                    | Set if unknown (unable to detect sizes) volumes should be printed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [useAvailable](#modules_items_anyOf_i1_oneOf_i20_useAvailable )     | No      | boolean          | No         | -                                                                    | Use f_bavail (lpFreeBytesAvailableToCaller for Windows) instead of f_bfree to calculate used bytes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [percent](#modules_items_anyOf_i1_oneOf_i20_percent )               | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i20_key )                       | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i20_keyColor )             | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i20_keyIcon )               | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i20_keyWidth )             | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i20_outputColor )       | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i20_format )                 | No      | string           | No         | In #/$defs/diskFormat                                                | Output format of the module \`Disk\`. See Wiki for formatting syntax<br />    1. {size-used}: Size used<br />    2. {size-total}: Size total<br />    3. {size-percentage}: Size percentage num<br />    4. {files-used}: Files used<br />    5. {files-total}: Files total<br />    6. {files-percentage}: Files percentage num<br />    7. {is-external}: True if external volume<br />    8. {is-hidden}: True if hidden volume<br />    9. {filesystem}: Filesystem<br />    10. {name}: Label / name<br />    11. {is-readonly}: True if read-only<br />    12. {create-time}: Create time in local timezone<br />    13. {size-percentage-bar}: Size percentage bar<br />    14. {files-percentage-bar}: Files percentage bar<br />    15. {days}: Days after creation<br />    16. {hours}: Hours after creation<br />    17. {minutes}: Minutes after creation<br />    18. {seconds}: Seconds after creation<br />    19. {milliseconds}: Milliseconds after creation<br />    20. {mountpoint}: Mount point / drive letter<br />    21. {mount-from}: Mount from (device path) |

###### <a name="modules_items_anyOf_i1_oneOf_i20_type"></a>5.1.2.21.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print partitions, space usage, disk type, etc

Specific value: `"disk"`

###### <a name="modules_items_anyOf_i1_oneOf_i20_folders"></a>5.1.2.21.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > folders`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A colon (semicolon on Windows) separated list of folder paths for the disk output
Default: auto detection using mount-points
This option overrides other `show*` options

###### <a name="modules_items_anyOf_i1_oneOf_i20_showExternal"></a>5.1.2.21.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showExternal`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Set if external volume should be printed

###### <a name="modules_items_anyOf_i1_oneOf_i20_showHidden"></a>5.1.2.21.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showHidden`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if hidden volumes should be printed

###### <a name="modules_items_anyOf_i1_oneOf_i20_showSubvolumes"></a>5.1.2.21.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showSubvolumes`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if subvolumes should be printed

###### <a name="modules_items_anyOf_i1_oneOf_i20_showReadOnly"></a>5.1.2.21.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showReadOnly`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if read only volumes should be printed

###### <a name="modules_items_anyOf_i1_oneOf_i20_showUnknown"></a>5.1.2.21.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > showUnknown`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if unknown (unable to detect sizes) volumes should be printed

###### <a name="modules_items_anyOf_i1_oneOf_i20_useAvailable"></a>5.1.2.21.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > useAvailable`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Use f_bavail (lpFreeBytesAvailableToCaller for Windows) instead of f_bfree to calculate used bytes

###### <a name="modules_items_anyOf_i1_oneOf_i20_percent"></a>5.1.2.21.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i20_key"></a>5.1.2.21.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i20_keyColor"></a>5.1.2.21.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i20_keyIcon"></a>5.1.2.21.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i20_keyWidth"></a>5.1.2.21.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i20_outputColor"></a>5.1.2.21.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i20_format"></a>5.1.2.21.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Disk > format`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/diskFormat |

**Description:** Output format of the module `Disk`. See Wiki for formatting syntax
    1. {size-used}: Size used
    2. {size-total}: Size total
    3. {size-percentage}: Size percentage num
    4. {files-used}: Files used
    5. {files-total}: Files total
    6. {files-percentage}: Files percentage num
    7. {is-external}: True if external volume
    8. {is-hidden}: True if hidden volume
    9. {filesystem}: Filesystem
    10. {name}: Label / name
    11. {is-readonly}: True if read-only
    12. {create-time}: Create time in local timezone
    13. {size-percentage-bar}: Size percentage bar
    14. {files-percentage-bar}: Files percentage bar
    15. {days}: Days after creation
    16. {hours}: Hours after creation
    17. {minutes}: Minutes after creation
    18. {seconds}: Seconds after creation
    19. {milliseconds}: Milliseconds after creation
    20. {mountpoint}: Mount point / drive letter
    21. {mount-from}: Mount from (device path)

##### <a name="modules_items_anyOf_i1_oneOf_i21"></a>5.1.2.22. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO`

**Title:** DiskIO

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i21_type )               | No      | const            | No         | -                                                                    | Print physical disk I/O throughput                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [namePrefix](#modules_items_anyOf_i1_oneOf_i21_namePrefix )   | No      | string           | No         | -                                                                    | Show disks with given name prefix only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [detectTotal](#modules_items_anyOf_i1_oneOf_i21_detectTotal ) | No      | boolean          | No         | -                                                                    | Detect total bytes instead of current rate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [waitTime](#modules_items_anyOf_i1_oneOf_i21_waitTime )       | No      | integer          | No         | -                                                                    | Wait time (in ms). Disk I/O = (totalBytesEnd - totalBytesStart) / waitTime                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [key](#modules_items_anyOf_i1_oneOf_i21_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i21_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i21_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i21_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i21_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [format](#modules_items_anyOf_i1_oneOf_i21_format )           | No      | string           | No         | In #/$defs/diskioFormat                                              | Output format of the module \`DiskIO\`. See Wiki for formatting syntax<br />    1. {size-read}: Size of data read [per second] (formatted)<br />    2. {size-written}: Size of data written [per second] (formatted)<br />    3. {name}: Device name<br />    4. {dev-path}: Device raw file path<br />    5. {bytes-read}: Size of data read [per second] (in bytes)<br />    6. {bytes-written}: Size of data written [per second] (in bytes)<br />    7. {read-count}: Number of reads<br />    8. {write-count}: Number of writes |

###### <a name="modules_items_anyOf_i1_oneOf_i21_type"></a>5.1.2.22.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print physical disk I/O throughput

Specific value: `"diskio"`

###### <a name="modules_items_anyOf_i1_oneOf_i21_namePrefix"></a>5.1.2.22.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > namePrefix`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show disks with given name prefix only

###### <a name="modules_items_anyOf_i1_oneOf_i21_detectTotal"></a>5.1.2.22.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > detectTotal`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Detect total bytes instead of current rate

###### <a name="modules_items_anyOf_i1_oneOf_i21_waitTime"></a>5.1.2.22.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > waitTime`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Wait time (in ms). Disk I/O = (totalBytesEnd - totalBytesStart) / waitTime

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

###### <a name="modules_items_anyOf_i1_oneOf_i21_key"></a>5.1.2.22.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i21_keyColor"></a>5.1.2.22.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i21_keyIcon"></a>5.1.2.22.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i21_keyWidth"></a>5.1.2.22.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i21_outputColor"></a>5.1.2.22.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i21_format"></a>5.1.2.22.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DiskIO > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/diskioFormat |

**Description:** Output format of the module `DiskIO`. See Wiki for formatting syntax
    1. {size-read}: Size of data read [per second] (formatted)
    2. {size-written}: Size of data written [per second] (formatted)
    3. {name}: Device name
    4. {dev-path}: Device raw file path
    5. {bytes-read}: Size of data read [per second] (in bytes)
    6. {bytes-written}: Size of data written [per second] (in bytes)
    7. {read-count}: Number of reads
    8. {write-count}: Number of writes

##### <a name="modules_items_anyOf_i1_oneOf_i22"></a>5.1.2.23. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment`

**Title:** Desktop Environment

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                          | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                          |
| --------------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i22_type )                                 | No      | const            | No         | -                                                                    | Print desktop environment name                                                                                                                                                             |
| - [slowVersionDetection](#modules_items_anyOf_i1_oneOf_i22_slowVersionDetection ) | No      | boolean          | No         | -                                                                    | Set if DE version should be detected with slow operations.<br />Should be unnecessary for most cases.                                                                                      |
| - [key](#modules_items_anyOf_i1_oneOf_i22_key )                                   | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                          |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i22_keyColor )                         | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                          |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i22_keyIcon )                           | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i22_keyWidth )                         | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                 |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i22_outputColor )                   | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                     |
| - [format](#modules_items_anyOf_i1_oneOf_i22_format )                             | No      | string           | No         | In #/$defs/deFormat                                                  | Output format of the module \`DE\`. See Wiki for formatting syntax<br />    1. {process-name}: DE process name<br />    2. {pretty-name}: DE pretty name<br />    3. {version}: DE version |

###### <a name="modules_items_anyOf_i1_oneOf_i22_type"></a>5.1.2.23.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print desktop environment name

Specific value: `"de"`

###### <a name="modules_items_anyOf_i1_oneOf_i22_slowVersionDetection"></a>5.1.2.23.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > slowVersionDetection`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `"false"` |

**Description:** Set if DE version should be detected with slow operations.
Should be unnecessary for most cases.

###### <a name="modules_items_anyOf_i1_oneOf_i22_key"></a>5.1.2.23.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i22_keyColor"></a>5.1.2.23.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i22_keyIcon"></a>5.1.2.23.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i22_keyWidth"></a>5.1.2.23.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i22_outputColor"></a>5.1.2.23.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i22_format"></a>5.1.2.23.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Desktop Environment > format`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/deFormat |

**Description:** Output format of the module `DE`. See Wiki for formatting syntax
    1. {process-name}: DE process name
    2. {pretty-name}: DE pretty name
    3. {version}: DE version

##### <a name="modules_items_anyOf_i1_oneOf_i23"></a>5.1.2.24. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS`

**Title:** DNS

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                    |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i23_type )               | No      | const            | No         | -                                                                    | Print DNS servers                                                                                    |
| - [showType](#modules_items_anyOf_i1_oneOf_i23_showType )       | No      | enum (of string) | No         | -                                                                    | Specify the type of DNS servers should be detected                                                   |
| - [key](#modules_items_anyOf_i1_oneOf_i23_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                    |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i23_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                    |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i23_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                          |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i23_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                           |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i23_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                               |
| - [format](#modules_items_anyOf_i1_oneOf_i23_format )           | No      | string           | No         | In #/$defs/dnsFormat                                                 | Output format of the module \`DNS\`. See Wiki for formatting syntax<br />    1. {result}: DNS result |

###### <a name="modules_items_anyOf_i1_oneOf_i23_type"></a>5.1.2.24.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print DNS servers

Specific value: `"dns"`

###### <a name="modules_items_anyOf_i1_oneOf_i23_showType"></a>5.1.2.24.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > showType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"both"`           |

**Description:** Specify the type of DNS servers should be detected

Must be one of:
* "ipv4"
* "ipv6"
* "both"

###### <a name="modules_items_anyOf_i1_oneOf_i23_key"></a>5.1.2.24.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i23_keyColor"></a>5.1.2.24.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i23_keyIcon"></a>5.1.2.24.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i23_keyWidth"></a>5.1.2.24.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i23_outputColor"></a>5.1.2.24.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i23_format"></a>5.1.2.24.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > DNS > format`

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/dnsFormat |

**Description:** Output format of the module `DNS`. See Wiki for formatting syntax
    1. {result}: DNS result

##### <a name="modules_items_anyOf_i1_oneOf_i24"></a>5.1.2.25. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor`

**Title:** Editor

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i24_type )               | No      | const            | No         | -                                                                    | Print information of the default editor ($VISUAL or $EDITOR)                                                                                                                                                                                                            |
| - [percent](#modules_items_anyOf_i1_oneOf_i24_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                        |
| - [key](#modules_items_anyOf_i1_oneOf_i24_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                       |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i24_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                       |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i24_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                             |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i24_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                              |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i24_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                  |
| - [format](#modules_items_anyOf_i1_oneOf_i24_format )           | No      | string           | No         | In #/$defs/editorFormat                                              | Output format of the module \`Editor\`. See Wiki for formatting syntax<br />    1. {type}: Type (Visual / Editor)<br />    2. {name}: Name<br />    3. {exe-name}: Exe name of real path<br />    4. {full-path}: Full path of real path<br />    5. {version}: Version |

###### <a name="modules_items_anyOf_i1_oneOf_i24_type"></a>5.1.2.25.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print information of the default editor ($VISUAL or $EDITOR)

Specific value: `"editor"`

###### <a name="modules_items_anyOf_i1_oneOf_i24_percent"></a>5.1.2.25.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i24_key"></a>5.1.2.25.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i24_keyColor"></a>5.1.2.25.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i24_keyIcon"></a>5.1.2.25.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i24_keyWidth"></a>5.1.2.25.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i24_outputColor"></a>5.1.2.25.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i24_format"></a>5.1.2.25.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Editor > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/editorFormat |

**Description:** Output format of the module `Editor`. See Wiki for formatting syntax
    1. {type}: Type (Visual / Editor)
    2. {name}: Name
    3. {exe-name}: Exe name of real path
    4. {full-path}: Full path of real path
    5. {version}: Version

##### <a name="modules_items_anyOf_i1_oneOf_i25"></a>5.1.2.26. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font`

**Title:** Font

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                       |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i25_type )               | No      | const            | No         | -                                                                    | Print system font names                                                                                                                                                                                                                 |
| - [percent](#modules_items_anyOf_i1_oneOf_i25_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                        |
| - [key](#modules_items_anyOf_i1_oneOf_i25_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                       |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i25_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                       |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i25_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                             |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i25_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                              |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i25_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                  |
| - [format](#modules_items_anyOf_i1_oneOf_i25_format )           | No      | string           | No         | In #/$defs/fontFormat                                                | Output format of the module \`Font\`. See Wiki for formatting syntax<br />    1. {font1}: Font 1<br />    2. {font2}: Font 2<br />    3. {font3}: Font 3<br />    4. {font4}: Font 4<br />    5. {combined}: Combined fonts for display |

###### <a name="modules_items_anyOf_i1_oneOf_i25_type"></a>5.1.2.26.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system font names

Specific value: `"font"`

###### <a name="modules_items_anyOf_i1_oneOf_i25_percent"></a>5.1.2.26.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i25_key"></a>5.1.2.26.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i25_keyColor"></a>5.1.2.26.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i25_keyIcon"></a>5.1.2.26.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i25_keyWidth"></a>5.1.2.26.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i25_outputColor"></a>5.1.2.26.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i25_format"></a>5.1.2.26.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Font > format`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/fontFormat |

**Description:** Output format of the module `Font`. See Wiki for formatting syntax
    1. {font1}: Font 1
    2. {font2}: Font 2
    3. {font3}: Font 3
    4. {font4}: Font 4
    5. {combined}: Combined fonts for display

##### <a name="modules_items_anyOf_i1_oneOf_i26"></a>5.1.2.27. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad`

**Title:** Gamepad

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                          |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i26_type )               | No      | const            | No         | -                                                                    | List connected gamepads                                                                                                                                                                                                                                    |
| - [percent](#modules_items_anyOf_i1_oneOf_i26_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                           |
| - [key](#modules_items_anyOf_i1_oneOf_i26_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                          |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i26_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                          |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i26_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i26_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                 |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i26_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                     |
| - [format](#modules_items_anyOf_i1_oneOf_i26_format )           | No      | string           | No         | In #/$defs/gamepadFormat                                             | Output format of the module \`Gamepad\`. See Wiki for formatting syntax<br />    1. {name}: Name<br />    2. {serial}: Serial number<br />    3. {battery-percentage}: Battery percentage num<br />    4. {battery-percentage-bar}: Battery percentage bar |

###### <a name="modules_items_anyOf_i1_oneOf_i26_type"></a>5.1.2.27.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List connected gamepads

Specific value: `"gamepad"`

###### <a name="modules_items_anyOf_i1_oneOf_i26_percent"></a>5.1.2.27.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i26_key"></a>5.1.2.27.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i26_keyColor"></a>5.1.2.27.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i26_keyIcon"></a>5.1.2.27.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i26_keyWidth"></a>5.1.2.27.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i26_outputColor"></a>5.1.2.27.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i26_format"></a>5.1.2.27.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Gamepad > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/gamepadFormat |

**Description:** Output format of the module `Gamepad`. See Wiki for formatting syntax
    1. {name}: Name
    2. {serial}: Serial number
    3. {battery-percentage}: Battery percentage num
    4. {battery-percentage-bar}: Battery percentage bar

##### <a name="modules_items_anyOf_i1_oneOf_i27"></a>5.1.2.28. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU`

**Title:** GPU

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i27_type )                       | No      | const            | No         | -                                                                    | Print GPU names, graphic memory size, type, etc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [temp](#modules_items_anyOf_i1_oneOf_i27_temp )                       | No      | object           | No         | Same as [temp](#modules_items_anyOf_i1_oneOf_i1_temp )               | Detect and display temperature if supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [driverSpecific](#modules_items_anyOf_i1_oneOf_i27_driverSpecific )   | No      | boolean          | No         | -                                                                    | Use driver specific method to detect more detailed GPU information (memory usage, core count, etc)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [detectionMethod](#modules_items_anyOf_i1_oneOf_i27_detectionMethod ) | No      | enum (of string) | No         | -                                                                    | Force using a specified method to detect GPUs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [hideType](#modules_items_anyOf_i1_oneOf_i27_hideType )               | No      | enum (of string) | No         | -                                                                    | Specify the type of GPUs should not be printed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [key](#modules_items_anyOf_i1_oneOf_i27_key )                         | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i27_keyColor )               | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i27_keyIcon )                 | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i27_keyWidth )               | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i27_outputColor )         | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i27_format )                   | No      | string           | No         | In #/$defs/gpuFormat                                                 | Output format of the module \`GPU\`. See Wiki for formatting syntax<br />    1. {vendor}: GPU vendor<br />    2. {name}: GPU name<br />    3. {driver}: GPU driver<br />    4. {temperature}: GPU temperature<br />    5. {core-count}: GPU core count<br />    6. {type}: GPU type<br />    7. {dedicated-total}: GPU total dedicated memory<br />    8. {dedicated-used}: GPU used dedicated memory<br />    9. {shared-total}: GPU total shared memory<br />    10. {shared-used}: GPU used shared memory<br />    11. {platform-api}: The platform API used when detecting the GPU<br />    12. {frequency}: Current frequency in GHz<br />    13. {index}: GPU vendor specific index<br />    14. {dedicated-percentage-num}: Dedicated memory usage percentage num<br />    15. {dedicated-percentage-bar}: Dedicated memory usage percentage bar<br />    16. {shared-percentage-num}: Shared memory usage percentage num<br />    17. {shared-percentage-bar}: Shared memory usage percentage bar<br />    18. {core-usage-num}: Core usage percentage num<br />    19. {core-usage-bar}: Core usage percentage bar<br />    20. {memory-type}: Memory type (Windows only) |

###### <a name="modules_items_anyOf_i1_oneOf_i27_type"></a>5.1.2.28.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print GPU names, graphic memory size, type, etc

Specific value: `"gpu"`

###### <a name="modules_items_anyOf_i1_oneOf_i27_temp"></a>5.1.2.28.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > temp`

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [temp](#modules_items_anyOf_i1_oneOf_i1_temp) |

**Description:** Detect and display temperature if supported

###### <a name="modules_items_anyOf_i1_oneOf_i27_driverSpecific"></a>5.1.2.28.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > driverSpecific`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Use driver specific method to detect more detailed GPU information (memory usage, core count, etc)

###### <a name="modules_items_anyOf_i1_oneOf_i27_detectionMethod"></a>5.1.2.28.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > detectionMethod`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"auto"`           |

**Description:** Force using a specified method to detect GPUs

Must be one of:
* "auto"
* "pci"
* "vulkan"
* "opencl"
* "opengl"

###### <a name="modules_items_anyOf_i1_oneOf_i27_hideType"></a>5.1.2.28.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > hideType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"none"`           |

**Description:** Specify the type of GPUs should not be printed

Must be one of:
* "integrated"
* "discrete"
* "unknown"
* "none"

###### <a name="modules_items_anyOf_i1_oneOf_i27_key"></a>5.1.2.28.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i27_keyColor"></a>5.1.2.28.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i27_keyIcon"></a>5.1.2.28.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i27_keyWidth"></a>5.1.2.28.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i27_outputColor"></a>5.1.2.28.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i27_format"></a>5.1.2.28.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > GPU > format`

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/gpuFormat |

**Description:** Output format of the module `GPU`. See Wiki for formatting syntax
    1. {vendor}: GPU vendor
    2. {name}: GPU name
    3. {driver}: GPU driver
    4. {temperature}: GPU temperature
    5. {core-count}: GPU core count
    6. {type}: GPU type
    7. {dedicated-total}: GPU total dedicated memory
    8. {dedicated-used}: GPU used dedicated memory
    9. {shared-total}: GPU total shared memory
    10. {shared-used}: GPU used shared memory
    11. {platform-api}: The platform API used when detecting the GPU
    12. {frequency}: Current frequency in GHz
    13. {index}: GPU vendor specific index
    14. {dedicated-percentage-num}: Dedicated memory usage percentage num
    15. {dedicated-percentage-bar}: Dedicated memory usage percentage bar
    16. {shared-percentage-num}: Shared memory usage percentage num
    17. {shared-percentage-bar}: Shared memory usage percentage bar
    18. {core-usage-num}: Core usage percentage num
    19. {core-usage-bar}: Core usage percentage bar
    20. {memory-type}: Memory type (Windows only)

##### <a name="modules_items_anyOf_i1_oneOf_i28"></a>5.1.2.29. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host`

**Title:** Host

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i28_type )               | No      | const            | No         | -                                                                    | Print product name of your computer                                                                                                                                                                                                                                                                                                |
| - [key](#modules_items_anyOf_i1_oneOf_i28_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i28_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i28_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i28_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i28_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i28_format )           | No      | string           | No         | In #/$defs/hostFormat                                                | Output format of the module \`Host\`. See Wiki for formatting syntax<br />    1. {family}: Product family<br />    2. {name}: Product name<br />    3. {version}: Product version<br />    4. {sku}: Product sku<br />    5. {vendor}: Product vendor<br />    6. {serial}: Product serial number<br />    7. {uuid}: Product uuid |

###### <a name="modules_items_anyOf_i1_oneOf_i28_type"></a>5.1.2.29.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print product name of your computer

Specific value: `"host"`

###### <a name="modules_items_anyOf_i1_oneOf_i28_key"></a>5.1.2.29.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i28_keyColor"></a>5.1.2.29.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i28_keyIcon"></a>5.1.2.29.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i28_keyWidth"></a>5.1.2.29.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i28_outputColor"></a>5.1.2.29.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i28_format"></a>5.1.2.29.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Host > format`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/hostFormat |

**Description:** Output format of the module `Host`. See Wiki for formatting syntax
    1. {family}: Product family
    2. {name}: Product name
    3. {version}: Product version
    4. {sku}: Product sku
    5. {vendor}: Product vendor
    6. {serial}: Product serial number
    7. {uuid}: Product uuid

##### <a name="modules_items_anyOf_i1_oneOf_i29"></a>5.1.2.30. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons`

**Title:** Icons

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                           |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i29_type )               | No      | const            | No         | -                                                                    | Print icon style name                                                                                                                       |
| - [key](#modules_items_anyOf_i1_oneOf_i29_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                           |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i29_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                           |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i29_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                 |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i29_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                  |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i29_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                      |
| - [format](#modules_items_anyOf_i1_oneOf_i29_format )           | No      | string           | No         | In #/$defs/iconsFormat                                               | Output format of the module \`Icons\`. See Wiki for formatting syntax<br />    1. {icons1}: Icons part 1<br />    2. {icons2}: Icons part 2 |

###### <a name="modules_items_anyOf_i1_oneOf_i29_type"></a>5.1.2.30.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print icon style name

Specific value: `"icons"`

###### <a name="modules_items_anyOf_i1_oneOf_i29_key"></a>5.1.2.30.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i29_keyColor"></a>5.1.2.30.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i29_keyIcon"></a>5.1.2.30.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i29_keyWidth"></a>5.1.2.30.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i29_outputColor"></a>5.1.2.30.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i29_format"></a>5.1.2.30.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Icons > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/iconsFormat |

**Description:** Output format of the module `Icons`. See Wiki for formatting syntax
    1. {icons1}: Icons part 1
    2. {icons2}: Icons part 2

##### <a name="modules_items_anyOf_i1_oneOf_i30"></a>5.1.2.31. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System`

**Title:** Init System

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                          |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i30_type )               | No      | const            | No         | -                                                                    | Print init system (pid 1) name and version                                                                                                                                                                                                 |
| - [key](#modules_items_anyOf_i1_oneOf_i30_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                          |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i30_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                          |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i30_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i30_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                 |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i30_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                     |
| - [format](#modules_items_anyOf_i1_oneOf_i30_format )           | No      | string           | No         | In #/$defs/initsystemFormat                                          | Output format of the module \`InitSystem\`. See Wiki for formatting syntax<br />    1. {name}: Init system name<br />    2. {exe}: Init system exe path<br />    3. {version}: Init system version path<br />    4. {pid}: Init system pid |

###### <a name="modules_items_anyOf_i1_oneOf_i30_type"></a>5.1.2.31.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print init system (pid 1) name and version

Specific value: `"initsystem"`

###### <a name="modules_items_anyOf_i1_oneOf_i30_key"></a>5.1.2.31.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i30_keyColor"></a>5.1.2.31.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i30_keyIcon"></a>5.1.2.31.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i30_keyWidth"></a>5.1.2.31.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i30_outputColor"></a>5.1.2.31.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i30_format"></a>5.1.2.31.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Init System > format`

|                |                          |
| -------------- | ------------------------ |
| **Type**       | `string`                 |
| **Required**   | No                       |
| **Defined in** | #/$defs/initsystemFormat |

**Description:** Output format of the module `InitSystem`. See Wiki for formatting syntax
    1. {name}: Init system name
    2. {exe}: Init system exe path
    3. {version}: Init system version path
    4. {pid}: Init system pid

##### <a name="modules_items_anyOf_i1_oneOf_i31"></a>5.1.2.32. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel`

**Title:** Kernel

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i31_type )               | No      | const            | No         | -                                                                    | Print system kernel version                                                                                                                                                                                                                                                            |
| - [key](#modules_items_anyOf_i1_oneOf_i31_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i31_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i31_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i31_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i31_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i31_format )           | No      | string           | No         | In #/$defs/kernelFormat                                              | Output format of the module \`Kernel\`. See Wiki for formatting syntax<br />    1. {sysname}: Sysname<br />    2. {release}: Release<br />    3. {version}: Version<br />    4. {arch}: Architecture<br />    5. {display-version}: Display version<br />    6. {page-size}: Page size |

###### <a name="modules_items_anyOf_i1_oneOf_i31_type"></a>5.1.2.32.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system kernel version

Specific value: `"kernel"`

###### <a name="modules_items_anyOf_i1_oneOf_i31_key"></a>5.1.2.32.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i31_keyColor"></a>5.1.2.32.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i31_keyIcon"></a>5.1.2.32.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i31_keyWidth"></a>5.1.2.32.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i31_outputColor"></a>5.1.2.32.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i31_format"></a>5.1.2.32.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Kernel > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/kernelFormat |

**Description:** Output format of the module `Kernel`. See Wiki for formatting syntax
    1. {sysname}: Sysname
    2. {release}: Release
    3. {version}: Version
    4. {arch}: Architecture
    5. {display-version}: Display version
    6. {page-size}: Page size

##### <a name="modules_items_anyOf_i1_oneOf_i32"></a>5.1.2.33. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager`

**Title:** Login Manager

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                  |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i32_type )               | No      | const            | No         | -                                                                    | Print login manager (desktop manager) name and version                                                                                                             |
| - [key](#modules_items_anyOf_i1_oneOf_i32_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i32_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i32_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i32_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i32_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i32_format )           | No      | string           | No         | In #/$defs/lmFormat                                                  | Output format of the module \`LM\`. See Wiki for formatting syntax<br />    1. {service}: LM service<br />    2. {type}: LM type<br />    3. {version}: LM version |

###### <a name="modules_items_anyOf_i1_oneOf_i32_type"></a>5.1.2.33.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print login manager (desktop manager) name and version

Specific value: `"lm"`

###### <a name="modules_items_anyOf_i1_oneOf_i32_key"></a>5.1.2.33.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i32_keyColor"></a>5.1.2.33.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i32_keyIcon"></a>5.1.2.33.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i32_keyWidth"></a>5.1.2.33.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i32_outputColor"></a>5.1.2.33.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i32_format"></a>5.1.2.33.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Login Manager > format`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/lmFormat |

**Description:** Output format of the module `LM`. See Wiki for formatting syntax
    1. {service}: LM service
    2. {type}: LM type
    3. {version}: LM version

##### <a name="modules_items_anyOf_i1_oneOf_i33"></a>5.1.2.34. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP`

**Title:** Local IP

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                  | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i33_type )                         | No      | const            | No         | -                                                                    | List local IP addresses (v4 or v6), MAC addresses, etc                                                                                                                                                                                                                                                                                                                               |
| - [showIpv4](#modules_items_anyOf_i1_oneOf_i33_showIpv4 )                 | No      | boolean          | No         | -                                                                    | Show IPv4 addresses                                                                                                                                                                                                                                                                                                                                                                  |
| - [showIpv6](#modules_items_anyOf_i1_oneOf_i33_showIpv6 )                 | No      | boolean          | No         | -                                                                    | Show IPv6 addresses                                                                                                                                                                                                                                                                                                                                                                  |
| - [showSpeed](#modules_items_anyOf_i1_oneOf_i33_showSpeed )               | No      | boolean          | No         | -                                                                    | Show ethernet rx speed                                                                                                                                                                                                                                                                                                                                                               |
| - [showMtu](#modules_items_anyOf_i1_oneOf_i33_showMtu )                   | No      | boolean          | No         | -                                                                    | Show MTU                                                                                                                                                                                                                                                                                                                                                                             |
| - [showMac](#modules_items_anyOf_i1_oneOf_i33_showMac )                   | No      | boolean          | No         | -                                                                    | Show MAC addresses                                                                                                                                                                                                                                                                                                                                                                   |
| - [showLoop](#modules_items_anyOf_i1_oneOf_i33_showLoop )                 | No      | boolean          | No         | -                                                                    | Show loop back addresses (127.0.0.1)                                                                                                                                                                                                                                                                                                                                                 |
| - [showPrefixLen](#modules_items_anyOf_i1_oneOf_i33_showPrefixLen )       | No      | boolean          | No         | -                                                                    | Show network prefix length (/N)                                                                                                                                                                                                                                                                                                                                                      |
| - [showAllIps](#modules_items_anyOf_i1_oneOf_i33_showAllIps )             | No      | boolean          | No         | -                                                                    | Show all IPs bound to the same interface.<br />By default only the first IP is shown                                                                                                                                                                                                                                                                                                 |
| - [showFlags](#modules_items_anyOf_i1_oneOf_i33_showFlags )               | No      | boolean          | No         | -                                                                    | Show the interface's flags                                                                                                                                                                                                                                                                                                                                                           |
| - [compact](#modules_items_anyOf_i1_oneOf_i33_compact )                   | No      | boolean          | No         | -                                                                    | Show all IPs in one line                                                                                                                                                                                                                                                                                                                                                             |
| - [namePrefix](#modules_items_anyOf_i1_oneOf_i33_namePrefix )             | No      | string           | No         | -                                                                    | Show IPs with given name prefix only                                                                                                                                                                                                                                                                                                                                                 |
| - [defaultRouteOnly](#modules_items_anyOf_i1_oneOf_i33_defaultRouteOnly ) | No      | boolean          | No         | -                                                                    | Show ips that are used for default routing only                                                                                                                                                                                                                                                                                                                                      |
| - [key](#modules_items_anyOf_i1_oneOf_i33_key )                           | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                    |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i33_keyColor )                 | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                    |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i33_keyIcon )                   | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                          |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i33_keyWidth )                 | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                           |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i33_outputColor )           | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                               |
| - [format](#modules_items_anyOf_i1_oneOf_i33_format )                     | No      | string           | No         | In #/$defs/localipFormat                                             | Output format of the module \`LocalIp\`. See Wiki for formatting syntax<br />    1. {ipv4}: IPv4 address<br />    2. {ipv6}: IPv6 address<br />    3. {mac}: MAC address<br />    4. {ifname}: Interface name<br />    5. {is-default-route}: Is default route<br />    6. {mtu}: MTU size in bytes<br />    7. {speed}: Link speed (formatted)<br />    8. {flags}: Interface flags |

###### <a name="modules_items_anyOf_i1_oneOf_i33_type"></a>5.1.2.34.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List local IP addresses (v4 or v6), MAC addresses, etc

Specific value: `"localip"`

###### <a name="modules_items_anyOf_i1_oneOf_i33_showIpv4"></a>5.1.2.34.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv4`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show IPv4 addresses

###### <a name="modules_items_anyOf_i1_oneOf_i33_showIpv6"></a>5.1.2.34.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showIpv6`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show IPv6 addresses

###### <a name="modules_items_anyOf_i1_oneOf_i33_showSpeed"></a>5.1.2.34.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showSpeed`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show ethernet rx speed

###### <a name="modules_items_anyOf_i1_oneOf_i33_showMtu"></a>5.1.2.34.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMtu`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show MTU

###### <a name="modules_items_anyOf_i1_oneOf_i33_showMac"></a>5.1.2.34.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showMac`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show MAC addresses

###### <a name="modules_items_anyOf_i1_oneOf_i33_showLoop"></a>5.1.2.34.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showLoop`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show loop back addresses (127.0.0.1)

###### <a name="modules_items_anyOf_i1_oneOf_i33_showPrefixLen"></a>5.1.2.34.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showPrefixLen`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show network prefix length (/N)

###### <a name="modules_items_anyOf_i1_oneOf_i33_showAllIps"></a>5.1.2.34.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showAllIps`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show all IPs bound to the same interface.
By default only the first IP is shown

###### <a name="modules_items_anyOf_i1_oneOf_i33_showFlags"></a>5.1.2.34.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > showFlags`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show the interface's flags

###### <a name="modules_items_anyOf_i1_oneOf_i33_compact"></a>5.1.2.34.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > compact`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show all IPs in one line

###### <a name="modules_items_anyOf_i1_oneOf_i33_namePrefix"></a>5.1.2.34.12. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > namePrefix`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show IPs with given name prefix only

###### <a name="modules_items_anyOf_i1_oneOf_i33_defaultRouteOnly"></a>5.1.2.34.13. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > defaultRouteOnly`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show ips that are used for default routing only

###### <a name="modules_items_anyOf_i1_oneOf_i33_key"></a>5.1.2.34.14. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i33_keyColor"></a>5.1.2.34.15. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i33_keyIcon"></a>5.1.2.34.16. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i33_keyWidth"></a>5.1.2.34.17. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i33_outputColor"></a>5.1.2.34.18. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i33_format"></a>5.1.2.34.19. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Local IP > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/localipFormat |

**Description:** Output format of the module `LocalIp`. See Wiki for formatting syntax
    1. {ipv4}: IPv4 address
    2. {ipv6}: IPv6 address
    3. {mac}: MAC address
    4. {ifname}: Interface name
    5. {is-default-route}: Is default route
    6. {mtu}: MTU size in bytes
    7. {speed}: Link speed (formatted)
    8. {flags}: Interface flags

##### <a name="modules_items_anyOf_i1_oneOf_i34"></a>5.1.2.35. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg`

**Title:** Loadavg

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                     |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i34_type )               | No      | const            | No         | -                                                                    | Print system load averages                                                                                                                                                                                            |
| - [ndigits](#modules_items_anyOf_i1_oneOf_i34_ndigits )         | No      | integer          | No         | -                                                                    | Set the number of digits to keep after the decimal point                                                                                                                                                              |
| - [compact](#modules_items_anyOf_i1_oneOf_i34_compact )         | No      | boolean          | No         | -                                                                    | Show values in one line                                                                                                                                                                                               |
| - [percent](#modules_items_anyOf_i1_oneOf_i34_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                      |
| - [key](#modules_items_anyOf_i1_oneOf_i34_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                     |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i34_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                     |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i34_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                           |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i34_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                            |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i34_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                |
| - [format](#modules_items_anyOf_i1_oneOf_i34_format )           | No      | string           | No         | In #/$defs/loadavgFormat                                             | Output format of the module \`Loadavg\`. See Wiki for formatting syntax<br />    1. {loadavg1}: Load average over 1min<br />    2. {loadavg2}: Load average over 5min<br />    3. {loadavg3}: Load average over 15min |

###### <a name="modules_items_anyOf_i1_oneOf_i34_type"></a>5.1.2.35.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system load averages

Specific value: `"loadavg"`

###### <a name="modules_items_anyOf_i1_oneOf_i34_ndigits"></a>5.1.2.35.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > ndigits`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `2`       |

**Description:** Set the number of digits to keep after the decimal point

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |
| **Maximum**  | &le; 9 |

###### <a name="modules_items_anyOf_i1_oneOf_i34_compact"></a>5.1.2.35.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > compact`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show values in one line

###### <a name="modules_items_anyOf_i1_oneOf_i34_percent"></a>5.1.2.35.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i34_key"></a>5.1.2.35.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i34_keyColor"></a>5.1.2.35.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i34_keyIcon"></a>5.1.2.35.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i34_keyWidth"></a>5.1.2.35.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i34_outputColor"></a>5.1.2.35.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i34_format"></a>5.1.2.35.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Loadavg > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/loadavgFormat |

**Description:** Output format of the module `Loadavg`. See Wiki for formatting syntax
    1. {loadavg1}: Load average over 1min
    2. {loadavg2}: Load average over 5min
    3. {loadavg3}: Load average over 15min

##### <a name="modules_items_anyOf_i1_oneOf_i35"></a>5.1.2.36. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale`

**Title:** Locale

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                        |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i35_type )               | No      | const            | No         | -                                                                    | Print system locale name                                                                                 |
| - [key](#modules_items_anyOf_i1_oneOf_i35_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i35_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i35_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i35_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i35_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i35_format )           | No      | string           | No         | In #/$defs/localeFormat                                              | Output format of the module \`Locale\`. See Wiki for formatting syntax<br />    1. {result}: Locale code |

###### <a name="modules_items_anyOf_i1_oneOf_i35_type"></a>5.1.2.36.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system locale name

Specific value: `"locale"`

###### <a name="modules_items_anyOf_i1_oneOf_i35_key"></a>5.1.2.36.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i35_keyColor"></a>5.1.2.36.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i35_keyIcon"></a>5.1.2.36.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i35_keyWidth"></a>5.1.2.36.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i35_outputColor"></a>5.1.2.36.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i35_format"></a>5.1.2.36.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Locale > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/localeFormat |

**Description:** Output format of the module `Locale`. See Wiki for formatting syntax
    1. {result}: Locale code

##### <a name="modules_items_anyOf_i1_oneOf_i36"></a>5.1.2.37. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media`

**Title:** Media

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                              |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i36_type )               | No      | const            | No         | -                                                                    | Print song name of currently playing                                                                                                                                                                                                           |
| - [key](#modules_items_anyOf_i1_oneOf_i36_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                              |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i36_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                              |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i36_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                    |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i36_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                     |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i36_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                         |
| - [format](#modules_items_anyOf_i1_oneOf_i36_format )           | No      | string           | No         | In #/$defs/mediaFormat                                               | Output format of the module \`Media\`. See Wiki for formatting syntax<br />    1. {combined}: Pretty media name<br />    2. {title}: Media name<br />    3. {artist}: Artist name<br />    4. {album}: Album name<br />    5. {status}: Status |

###### <a name="modules_items_anyOf_i1_oneOf_i36_type"></a>5.1.2.37.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print song name of currently playing

Specific value: `"media"`

###### <a name="modules_items_anyOf_i1_oneOf_i36_key"></a>5.1.2.37.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i36_keyColor"></a>5.1.2.37.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i36_keyIcon"></a>5.1.2.37.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i36_keyWidth"></a>5.1.2.37.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i36_outputColor"></a>5.1.2.37.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i36_format"></a>5.1.2.37.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Media > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/mediaFormat |

**Description:** Output format of the module `Media`. See Wiki for formatting syntax
    1. {combined}: Pretty media name
    2. {title}: Media name
    3. {artist}: Artist name
    4. {album}: Album name
    5. {status}: Status

##### <a name="modules_items_anyOf_i1_oneOf_i37"></a>5.1.2.38. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory`

**Title:** Memory

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                        |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i37_type )               | No      | const            | No         | -                                                                    | Print system memory usage info                                                                                                                                                                                                           |
| - [percent](#modules_items_anyOf_i1_oneOf_i37_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i37_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i37_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i37_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i37_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i37_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i37_format )           | No      | string           | No         | In #/$defs/memoryFormat                                              | Output format of the module \`Memory\`. See Wiki for formatting syntax<br />    1. {used}: Used size<br />    2. {total}: Total size<br />    3. {percentage}: Percentage used (num)<br />    4. {percentage-bar}: Percentage used (bar) |

###### <a name="modules_items_anyOf_i1_oneOf_i37_type"></a>5.1.2.38.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system memory usage info

Specific value: `"memory"`

###### <a name="modules_items_anyOf_i1_oneOf_i37_percent"></a>5.1.2.38.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i37_key"></a>5.1.2.38.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i37_keyColor"></a>5.1.2.38.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i37_keyIcon"></a>5.1.2.38.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i37_keyWidth"></a>5.1.2.38.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i37_outputColor"></a>5.1.2.38.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i37_format"></a>5.1.2.38.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Memory > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/memoryFormat |

**Description:** Output format of the module `Memory`. See Wiki for formatting syntax
    1. {used}: Used size
    2. {total}: Total size
    3. {percentage}: Percentage used (num)
    4. {percentage-bar}: Percentage used (bar)

##### <a name="modules_items_anyOf_i1_oneOf_i38"></a>5.1.2.39. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor`

**Title:** Monitor

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i38_type )               | No      | const            | No         | -                                                                    | Alias of Display module (for backwards compatibility, deprecated)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [key](#modules_items_anyOf_i1_oneOf_i38_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i38_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i38_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i38_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i38_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [format](#modules_items_anyOf_i1_oneOf_i38_format )           | No      | string           | No         | In #/$defs/monitorFormat                                             | Output format of the module \`Monitor\`. See Wiki for formatting syntax<br />    1. {name}: Display name<br />    2. {width}: Native resolution width in pixels<br />    3. {height}: Native resolution height in pixels<br />    4. {physical-width}: Physical width in millimeters<br />    5. {physical-height}: Physical height in millimeters<br />    6. {inch}: Physical diagonal length in inches<br />    7. {ppi}: Pixels per inch (PPI)<br />    8. {manufacture-year}: Year of manufacturing<br />    9. {manufacture-week}: Nth week of manufacturing in the year<br />    10. {serial}: Serial number<br />    11. {refresh-rate}: Maximum refresh rate in Hz<br />    12. {hdr-compatible}: True if the display is HDR compatible |

###### <a name="modules_items_anyOf_i1_oneOf_i38_type"></a>5.1.2.39.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Alias of Display module (for backwards compatibility, deprecated)

Specific value: `"monitor"`

###### <a name="modules_items_anyOf_i1_oneOf_i38_key"></a>5.1.2.39.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i38_keyColor"></a>5.1.2.39.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i38_keyIcon"></a>5.1.2.39.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i38_keyWidth"></a>5.1.2.39.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i38_outputColor"></a>5.1.2.39.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i38_format"></a>5.1.2.39.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Monitor > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/monitorFormat |

**Description:** Output format of the module `Monitor`. See Wiki for formatting syntax
    1. {name}: Display name
    2. {width}: Native resolution width in pixels
    3. {height}: Native resolution height in pixels
    4. {physical-width}: Physical width in millimeters
    5. {physical-height}: Physical height in millimeters
    6. {inch}: Physical diagonal length in inches
    7. {ppi}: Pixels per inch (PPI)
    8. {manufacture-year}: Year of manufacturing
    9. {manufacture-week}: Nth week of manufacturing in the year
    10. {serial}: Serial number
    11. {refresh-rate}: Maximum refresh rate in Hz
    12. {hdr-compatible}: True if the display is HDR compatible

##### <a name="modules_items_anyOf_i1_oneOf_i39"></a>5.1.2.40. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO`

**Title:** NetIO

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                                  | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i39_type )                         | No      | const            | No         | -                                                                    | Print network I/O throughput                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [namePrefix](#modules_items_anyOf_i1_oneOf_i39_namePrefix )             | No      | string           | No         | -                                                                    | Show IPs with given name prefix only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [defaultRouteOnly](#modules_items_anyOf_i1_oneOf_i39_defaultRouteOnly ) | No      | boolean          | No         | -                                                                    | Show ips that are used for default routing only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - [detectTotal](#modules_items_anyOf_i1_oneOf_i39_detectTotal )           | No      | boolean          | No         | -                                                                    | Detect total bytes instead of current rate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [waitTime](#modules_items_anyOf_i1_oneOf_i39_waitTime )                 | No      | integer          | No         | -                                                                    | Wait time (in ms). Disk I/O = (totalBytesEnd - totalBytesStart) / waitTime                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [key](#modules_items_anyOf_i1_oneOf_i39_key )                           | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i39_keyColor )                 | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i39_keyIcon )                   | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i39_keyWidth )                 | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i39_outputColor )           | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [format](#modules_items_anyOf_i1_oneOf_i39_format )                     | No      | string           | No         | In #/$defs/netioFormat                                               | Output format of the module \`NetIO\`. See Wiki for formatting syntax<br />    1. {rx-size}: Size of data received [per second] (formatted)<br />    2. {tx-size}: Size of data sent [per second] (formatted)<br />    3. {ifname}: Interface name<br />    4. {is-default-route}: Is default route<br />    5. {rx-bytes}: Size of data received [per second] (in bytes)<br />    6. {tx-bytes}: Size of data sent [per second] (in bytes)<br />    7. {rx-packets}: Number of packets received [per second]<br />    8. {tx-packets}: Number of packets sent [per second]<br />    9. {rx-errors}: Number of errors received [per second]<br />    10. {tx-errors}: Number of errors sent [per second]<br />    11. {rx-drops}: Number of packets dropped when receiving [per second]<br />    12. {tx-drops}: Number of packets dropped when sending [per second] |

###### <a name="modules_items_anyOf_i1_oneOf_i39_type"></a>5.1.2.40.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print network I/O throughput

Specific value: `"netio"`

###### <a name="modules_items_anyOf_i1_oneOf_i39_namePrefix"></a>5.1.2.40.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > namePrefix`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show IPs with given name prefix only

###### <a name="modules_items_anyOf_i1_oneOf_i39_defaultRouteOnly"></a>5.1.2.40.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > defaultRouteOnly`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `true`    |

**Description:** Show ips that are used for default routing only

###### <a name="modules_items_anyOf_i1_oneOf_i39_detectTotal"></a>5.1.2.40.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > detectTotal`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Detect total bytes instead of current rate

###### <a name="modules_items_anyOf_i1_oneOf_i39_waitTime"></a>5.1.2.40.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > waitTime`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `200`     |

**Description:** Wait time (in ms). Disk I/O = (totalBytesEnd - totalBytesStart) / waitTime

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 1 |

###### <a name="modules_items_anyOf_i1_oneOf_i39_key"></a>5.1.2.40.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i39_keyColor"></a>5.1.2.40.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i39_keyIcon"></a>5.1.2.40.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i39_keyWidth"></a>5.1.2.40.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i39_outputColor"></a>5.1.2.40.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i39_format"></a>5.1.2.40.11. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > NetIO > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/netioFormat |

**Description:** Output format of the module `NetIO`. See Wiki for formatting syntax
    1. {rx-size}: Size of data received [per second] (formatted)
    2. {tx-size}: Size of data sent [per second] (formatted)
    3. {ifname}: Interface name
    4. {is-default-route}: Is default route
    5. {rx-bytes}: Size of data received [per second] (in bytes)
    6. {tx-bytes}: Size of data sent [per second] (in bytes)
    7. {rx-packets}: Number of packets received [per second]
    8. {tx-packets}: Number of packets sent [per second]
    9. {rx-errors}: Number of errors received [per second]
    10. {tx-errors}: Number of errors sent [per second]
    11. {rx-drops}: Number of packets dropped when receiving [per second]
    12. {tx-drops}: Number of packets dropped when sending [per second]

##### <a name="modules_items_anyOf_i1_oneOf_i40"></a>5.1.2.41. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL`

**Title:** OpenCL

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i40_type )               | No      | const            | No         | -                                                                    | Print highest OpenCL version supported by the GPU                                                                                                                                      |
| - [key](#modules_items_anyOf_i1_oneOf_i40_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i40_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i40_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i40_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i40_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i40_format )           | No      | string           | No         | In #/$defs/openclFormat                                              | Output format of the module \`OpenCL\`. See Wiki for formatting syntax<br />    1. {version}: Platform version<br />    2. {name}: Platform name<br />    3. {vendor}: Platform vendor |

###### <a name="modules_items_anyOf_i1_oneOf_i40_type"></a>5.1.2.41.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print highest OpenCL version supported by the GPU

Specific value: `"opencl"`

###### <a name="modules_items_anyOf_i1_oneOf_i40_key"></a>5.1.2.41.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i40_keyColor"></a>5.1.2.41.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i40_keyIcon"></a>5.1.2.41.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i40_keyWidth"></a>5.1.2.41.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i40_outputColor"></a>5.1.2.41.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i40_format"></a>5.1.2.41.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenCL > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/openclFormat |

**Description:** Output format of the module `OpenCL`. See Wiki for formatting syntax
    1. {version}: Platform version
    2. {name}: Platform name
    3. {vendor}: Platform vendor

##### <a name="modules_items_anyOf_i1_oneOf_i41"></a>5.1.2.42. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL`

**Title:** OpenGL

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i41_type )               | No      | const            | No         | -                                                                    | Print highest OpenGL version supported by the GPU                                                                                                                                                                                                                                      |
| - [library](#modules_items_anyOf_i1_oneOf_i41_library )         | No      | enum (of string) | No         | -                                                                    | Set the OpenGL context creation library to use                                                                                                                                                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i41_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i41_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i41_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i41_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i41_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i41_format )           | No      | string           | No         | In #/$defs/openglFormat                                              | Output format of the module \`OpenGL\`. See Wiki for formatting syntax<br />    1. {version}: OpenGL version<br />    2. {renderer}: OpenGL renderer<br />    3. {vendor}: OpenGL vendor<br />    4. {slv}: OpenGL shading language version<br />    5. {library}: OpenGL library used |

###### <a name="modules_items_anyOf_i1_oneOf_i41_type"></a>5.1.2.42.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print highest OpenGL version supported by the GPU

Specific value: `"opengl"`

###### <a name="modules_items_anyOf_i1_oneOf_i41_library"></a>5.1.2.42.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > library`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"auto"`           |

**Description:** Set the OpenGL context creation library to use

Must be one of:
* "auto"
* "egl"
* "glx"

###### <a name="modules_items_anyOf_i1_oneOf_i41_key"></a>5.1.2.42.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i41_keyColor"></a>5.1.2.42.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i41_keyIcon"></a>5.1.2.42.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i41_keyWidth"></a>5.1.2.42.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i41_outputColor"></a>5.1.2.42.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i41_format"></a>5.1.2.42.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > OpenGL > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/openglFormat |

**Description:** Output format of the module `OpenGL`. See Wiki for formatting syntax
    1. {version}: OpenGL version
    2. {renderer}: OpenGL renderer
    3. {vendor}: OpenGL vendor
    4. {slv}: OpenGL shading language version
    5. {library}: OpenGL library used

##### <a name="modules_items_anyOf_i1_oneOf_i42"></a>5.1.2.43. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System`

**Title:** Operating System

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i42_type )               | No      | const            | No         | -                                                                    | Print OS / or Linux distro name and version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [key](#modules_items_anyOf_i1_oneOf_i42_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i42_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i42_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i42_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i42_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i42_format )           | No      | string           | No         | In #/$defs/osFormat                                                  | Output format of the module \`OS\`. See Wiki for formatting syntax<br />    1. {sysname}: Name of the kernel<br />    2. {name}: Name of the OS<br />    3. {pretty-name}: Pretty name of the OS, if available<br />    4. {id}: ID of the OS<br />    5. {id-like}: ID like of the OS<br />    6. {variant}: Variant of the OS<br />    7. {variant-id}: Variant ID of the OS<br />    8. {version}: Version of the OS<br />    9. {version-id}: Version ID of the OS<br />    10. {codename}: Version codename of the OS<br />    11. {build-id}: Build ID of the OS<br />    12. {arch}: Architecture of the OS |

###### <a name="modules_items_anyOf_i1_oneOf_i42_type"></a>5.1.2.43.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print OS / or Linux distro name and version

Specific value: `"os"`

###### <a name="modules_items_anyOf_i1_oneOf_i42_key"></a>5.1.2.43.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i42_keyColor"></a>5.1.2.43.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i42_keyIcon"></a>5.1.2.43.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i42_keyWidth"></a>5.1.2.43.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i42_outputColor"></a>5.1.2.43.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i42_format"></a>5.1.2.43.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Operating System > format`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/osFormat |

**Description:** Output format of the module `OS`. See Wiki for formatting syntax
    1. {sysname}: Name of the kernel
    2. {name}: Name of the OS
    3. {pretty-name}: Pretty name of the OS, if available
    4. {id}: ID of the OS
    5. {id-like}: ID like of the OS
    6. {variant}: Variant of the OS
    7. {variant-id}: Variant ID of the OS
    8. {version}: Version of the OS
    9. {version-id}: Version ID of the OS
    10. {codename}: Version codename of the OS
    11. {build-id}: Build ID of the OS
    12. {arch}: Architecture of the OS

##### <a name="modules_items_anyOf_i1_oneOf_i43"></a>5.1.2.44. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages`

**Title:** Packages

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type                      | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | ------- | ------------------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i43_type )               | No      | const                     | No         | -                                                                    | List installed package managers and count of installed packages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [disabled](#modules_items_anyOf_i1_oneOf_i43_disabled )       | No      | array of enum (of string) | No         | -                                                                    | List of package managers to be disabled when detecting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [key](#modules_items_anyOf_i1_oneOf_i43_key )                 | No      | string                    | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i43_keyColor )       | No      | enum (of string)          | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i43_keyIcon )         | No      | string                    | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i43_keyWidth )       | No      | integer                   | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i43_outputColor ) | No      | enum (of string)          | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [format](#modules_items_anyOf_i1_oneOf_i43_format )           | No      | string                    | No         | In #/$defs/packagesFormat                                            | Output format of the module \`Packages\`. See Wiki for formatting syntax<br />    1. {all}: Number of all packages<br />    2. {pacman}: Number of pacman packages<br />    3. {pacman-branch}: Pacman branch on manjaro<br />    4. {dpkg}: Number of dpkg packages<br />    5. {rpm}: Number of rpm packages<br />    6. {emerge}: Number of emerge packages<br />    7. {eopkg}: Number of eopkg packages<br />    8. {xbps}: Number of xbps packages<br />    9. {nix-system}: Number of nix-system packages<br />    10. {nix-user}: Number of nix-user packages<br />    11. {nix-default}: Number of nix-default packages<br />    12. {apk}: Number of apk packages<br />    13. {pkg}: Number of pkg packages<br />    14. {flatpak-system}: Number of flatpak-system app packages<br />    15. {flatpak-user}: Number of flatpak-user app packages<br />    16. {snap}: Number of snap packages<br />    17. {brew}: Number of brew packages<br />    18. {brew-cask}: Number of brew-cask packages<br />    19. {macports}: Number of macports packages<br />    20. {scoop}: Number of scoop packages<br />    21. {choco}: Number of choco packages<br />    22. {pkgtool}: Number of pkgtool packages<br />    23. {paludis}: Number of paludis packages<br />    24. {winget}: Number of winget packages<br />    25. {opkg}: Number of opkg packages<br />    26. {am-system}: Number of am-system packages<br />    27. {sorcery}: Number of sorcery packages<br />    28. {lpkg}: Number of lpkg packages<br />    29. {lpkgbuild}: Number of lpkgbuild packages<br />    30. {guix-system}: Number of guix-system packages<br />    31. {guix-user}: Number of guix-user packages<br />    32. {guix-home}: Number of guix-home packages<br />    33. {linglong}: Number of linglong packages<br />    34. {pacstall}: Number of pacstall packages<br />    35. {mport}: Number of mport packages<br />    36. {qi}: Number of qi packages<br />    37. {am-user}: Number of am-user (aka appman) packages<br />    38. {pkgsrc}: Number of pkgsrc packages<br />    39. {hpkg-system}: Number of hpkg-system packages<br />    40. {hpkg-user}: Number of hpkg-user packages<br />    41. {pisi}: Number of pisi packages<br />    42. {soar}: Number of soar packages<br />    43. {nix-all}: Total number of all nix packages<br />    44. {flatpak-all}: Total number of all flatpak app packages<br />    45. {brew-all}: Total number of all brew packages<br />    46. {guix-all}: Total number of all guix packages<br />    47. {hpkg-all}: Total number of all hpkg packages |

###### <a name="modules_items_anyOf_i1_oneOf_i43_type"></a>5.1.2.44.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** List installed package managers and count of installed packages

Specific value: `"packages"`

###### <a name="modules_items_anyOf_i1_oneOf_i43_disabled"></a>5.1.2.44.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled`

|              |                             |
| ------------ | --------------------------- |
| **Type**     | `array of enum (of string)` |
| **Required** | No                          |
| **Default**  | `["winget"]`                |

**Description:** List of package managers to be disabled when detecting

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                    | Description |
| ------------------------------------------------------------------ | ----------- |
| [disabled items](#modules_items_anyOf_i1_oneOf_i43_disabled_items) | -           |

###### <a name="modules_items_anyOf_i1_oneOf_i43_disabled_items"></a>5.1.2.44.2.1. JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > disabled > disabled items

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:
* "am"
* "apk"
* "brew"
* "choco"
* "dpkg"
* "emerge"
* "eopkg"
* "flatpak"
* "guix"
* "hpkg"
* "linglong"
* "lpkg"
* "lpkgbuild"
* "macports"
* "mport"
* "nix"
* "opkg"
* "pacman"
* "pacstall"
* "paludis"
* "pisi"
* "pkg"
* "pkgtool"
* "qi"
* "rpm"
* "scoop"
* "snap"
* "sorcery"
* "winget"
* "xbps"

###### <a name="modules_items_anyOf_i1_oneOf_i43_key"></a>5.1.2.44.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i43_keyColor"></a>5.1.2.44.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i43_keyIcon"></a>5.1.2.44.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i43_keyWidth"></a>5.1.2.44.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i43_outputColor"></a>5.1.2.44.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i43_format"></a>5.1.2.44.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Packages > format`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/packagesFormat |

**Description:** Output format of the module `Packages`. See Wiki for formatting syntax
    1. {all}: Number of all packages
    2. {pacman}: Number of pacman packages
    3. {pacman-branch}: Pacman branch on manjaro
    4. {dpkg}: Number of dpkg packages
    5. {rpm}: Number of rpm packages
    6. {emerge}: Number of emerge packages
    7. {eopkg}: Number of eopkg packages
    8. {xbps}: Number of xbps packages
    9. {nix-system}: Number of nix-system packages
    10. {nix-user}: Number of nix-user packages
    11. {nix-default}: Number of nix-default packages
    12. {apk}: Number of apk packages
    13. {pkg}: Number of pkg packages
    14. {flatpak-system}: Number of flatpak-system app packages
    15. {flatpak-user}: Number of flatpak-user app packages
    16. {snap}: Number of snap packages
    17. {brew}: Number of brew packages
    18. {brew-cask}: Number of brew-cask packages
    19. {macports}: Number of macports packages
    20. {scoop}: Number of scoop packages
    21. {choco}: Number of choco packages
    22. {pkgtool}: Number of pkgtool packages
    23. {paludis}: Number of paludis packages
    24. {winget}: Number of winget packages
    25. {opkg}: Number of opkg packages
    26. {am-system}: Number of am-system packages
    27. {sorcery}: Number of sorcery packages
    28. {lpkg}: Number of lpkg packages
    29. {lpkgbuild}: Number of lpkgbuild packages
    30. {guix-system}: Number of guix-system packages
    31. {guix-user}: Number of guix-user packages
    32. {guix-home}: Number of guix-home packages
    33. {linglong}: Number of linglong packages
    34. {pacstall}: Number of pacstall packages
    35. {mport}: Number of mport packages
    36. {qi}: Number of qi packages
    37. {am-user}: Number of am-user (aka appman) packages
    38. {pkgsrc}: Number of pkgsrc packages
    39. {hpkg-system}: Number of hpkg-system packages
    40. {hpkg-user}: Number of hpkg-user packages
    41. {pisi}: Number of pisi packages
    42. {soar}: Number of soar packages
    43. {nix-all}: Total number of all nix packages
    44. {flatpak-all}: Total number of all flatpak app packages
    45. {brew-all}: Total number of all brew packages
    46. {guix-all}: Total number of all guix packages
    47. {hpkg-all}: Total number of all hpkg packages

##### <a name="modules_items_anyOf_i1_oneOf_i44"></a>5.1.2.45. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk`

**Title:** Physical Disk

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i44_type )               | No      | const            | No         | -                                                                    | Print physical disk information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [namePrefix](#modules_items_anyOf_i1_oneOf_i44_namePrefix )   | No      | string           | No         | -                                                                    | Show disks with given name prefix only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [temp](#modules_items_anyOf_i1_oneOf_i44_temp )               | No      | object           | No         | Same as [temp](#modules_items_anyOf_i1_oneOf_i1_temp )               | Detect and display temperature if supported                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [key](#modules_items_anyOf_i1_oneOf_i44_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i44_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i44_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i44_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i44_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [format](#modules_items_anyOf_i1_oneOf_i44_format )           | No      | string           | No         | In #/$defs/physicaldiskFormat                                        | Output format of the module \`PhysicalDisk\`. See Wiki for formatting syntax<br />    1. {size}: Device size (formatted)<br />    2. {name}: Device name<br />    3. {interconnect}: Device interconnect type<br />    4. {dev-path}: Device raw file path<br />    5. {serial}: Serial number<br />    6. {physical-type}: Device kind (SSD or HDD)<br />    7. {removable-type}: Device kind (Removable or Fixed)<br />    8. {readonly-type}: Device kind (Read-only or Read-write)<br />    9. {revision}: Product revision<br />    10. {temperature}: Device temperature (formatted) |

###### <a name="modules_items_anyOf_i1_oneOf_i44_type"></a>5.1.2.45.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print physical disk information

Specific value: `"physicaldisk"`

###### <a name="modules_items_anyOf_i1_oneOf_i44_namePrefix"></a>5.1.2.45.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > namePrefix`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Show disks with given name prefix only

###### <a name="modules_items_anyOf_i1_oneOf_i44_temp"></a>5.1.2.45.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > temp`

|                           |                                               |
| ------------------------- | --------------------------------------------- |
| **Type**                  | `combining`                                   |
| **Required**              | No                                            |
| **Additional properties** | Any type allowed                              |
| **Same definition as**    | [temp](#modules_items_anyOf_i1_oneOf_i1_temp) |

**Description:** Detect and display temperature if supported

###### <a name="modules_items_anyOf_i1_oneOf_i44_key"></a>5.1.2.45.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i44_keyColor"></a>5.1.2.45.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i44_keyIcon"></a>5.1.2.45.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i44_keyWidth"></a>5.1.2.45.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i44_outputColor"></a>5.1.2.45.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i44_format"></a>5.1.2.45.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Disk > format`

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/physicaldiskFormat |

**Description:** Output format of the module `PhysicalDisk`. See Wiki for formatting syntax
    1. {size}: Device size (formatted)
    2. {name}: Device name
    3. {interconnect}: Device interconnect type
    4. {dev-path}: Device raw file path
    5. {serial}: Serial number
    6. {physical-type}: Device kind (SSD or HDD)
    7. {removable-type}: Device kind (Removable or Fixed)
    8. {readonly-type}: Device kind (Read-only or Read-write)
    9. {revision}: Product revision
    10. {temperature}: Device temperature (formatted)

##### <a name="modules_items_anyOf_i1_oneOf_i45"></a>5.1.2.46. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory`

**Title:** Physical Memory

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i45_type )               | No      | const            | No         | -                                                                    | Print system physical memory devices                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [key](#modules_items_anyOf_i1_oneOf_i45_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i45_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i45_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i45_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i45_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i45_format )           | No      | string           | No         | In #/$defs/physicalmemoryFormat                                      | Output format of the module \`PhysicalMemory\`. See Wiki for formatting syntax<br />    1. {bytes}: Size (in bytes)<br />    2. {size}: Size formatted<br />    3. {max-speed}: Max speed (in MT/s)<br />    4. {running-speed}: Running speed (in MT/s)<br />    5. {type}: Type (DDR4, DDR5, etc.)<br />    6. {form-factor}: Form factor (SODIMM, DIMM, etc.)<br />    7. {locator}: Bank/Device Locator (BANK0/SIMM0, BANK0/SIMM1, etc.)<br />    8. {vendor}: Vendor<br />    9. {serial}: Serial number<br />    10. {part-number}: Part number<br />    11. {is-ecc-enabled}: True if ECC enabled |

###### <a name="modules_items_anyOf_i1_oneOf_i45_type"></a>5.1.2.46.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print system physical memory devices

Specific value: `"physicalmemory"`

###### <a name="modules_items_anyOf_i1_oneOf_i45_key"></a>5.1.2.46.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i45_keyColor"></a>5.1.2.46.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i45_keyIcon"></a>5.1.2.46.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i45_keyWidth"></a>5.1.2.46.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i45_outputColor"></a>5.1.2.46.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i45_format"></a>5.1.2.46.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Physical Memory > format`

|                |                              |
| -------------- | ---------------------------- |
| **Type**       | `string`                     |
| **Required**   | No                           |
| **Defined in** | #/$defs/physicalmemoryFormat |

**Description:** Output format of the module `PhysicalMemory`. See Wiki for formatting syntax
    1. {bytes}: Size (in bytes)
    2. {size}: Size formatted
    3. {max-speed}: Max speed (in MT/s)
    4. {running-speed}: Running speed (in MT/s)
    5. {type}: Type (DDR4, DDR5, etc.)
    6. {form-factor}: Form factor (SODIMM, DIMM, etc.)
    7. {locator}: Bank/Device Locator (BANK0/SIMM0, BANK0/SIMM1, etc.)
    8. {vendor}: Vendor
    9. {serial}: Serial number
    10. {part-number}: Part number
    11. {is-ecc-enabled}: True if ECC enabled

##### <a name="modules_items_anyOf_i1_oneOf_i46"></a>5.1.2.47. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player`

**Title:** Player

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                               |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i46_type )               | No      | const            | No         | -                                                                    | Print music player name                                                                                                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i46_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                               |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i46_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                               |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i46_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                     |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i46_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                      |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i46_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                          |
| - [format](#modules_items_anyOf_i1_oneOf_i46_format )           | No      | string           | No         | In #/$defs/playerFormat                                              | Output format of the module \`Player\`. See Wiki for formatting syntax<br />    1. {player}: Pretty player name<br />    2. {name}: Player name<br />    3. {id}: Player Identifier<br />    4. {url}: URL name |

###### <a name="modules_items_anyOf_i1_oneOf_i46_type"></a>5.1.2.47.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print music player name

Specific value: `"player"`

###### <a name="modules_items_anyOf_i1_oneOf_i46_key"></a>5.1.2.47.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i46_keyColor"></a>5.1.2.47.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i46_keyIcon"></a>5.1.2.47.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i46_keyWidth"></a>5.1.2.47.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i46_outputColor"></a>5.1.2.47.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i46_format"></a>5.1.2.47.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Player > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/playerFormat |

**Description:** Output format of the module `Player`. See Wiki for formatting syntax
    1. {player}: Pretty player name
    2. {name}: Player name
    3. {id}: Player Identifier
    4. {url}: URL name

##### <a name="modules_items_anyOf_i1_oneOf_i47"></a>5.1.2.48. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter`

**Title:** Power Adapter

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i47_type )               | No      | const            | No         | -                                                                    | Print power adapter name and charging watts                                                                                                                                                                                                                                                                                                                         |
| - [key](#modules_items_anyOf_i1_oneOf_i47_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                   |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i47_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                   |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i47_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                         |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i47_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                          |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i47_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                              |
| - [format](#modules_items_anyOf_i1_oneOf_i47_format )           | No      | string           | No         | In #/$defs/poweradapterFormat                                        | Output format of the module \`PowerAdapter\`. See Wiki for formatting syntax<br />    1. {watts}: Power adapter watts<br />    2. {name}: Power adapter name<br />    3. {manufacturer}: Power adapter manufacturer<br />    4. {model}: Power adapter model<br />    5. {description}: Power adapter description<br />    6. {serial}: Power adapter serial number |

###### <a name="modules_items_anyOf_i1_oneOf_i47_type"></a>5.1.2.48.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print power adapter name and charging watts

Specific value: `"poweradapter"`

###### <a name="modules_items_anyOf_i1_oneOf_i47_key"></a>5.1.2.48.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i47_keyColor"></a>5.1.2.48.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i47_keyIcon"></a>5.1.2.48.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i47_keyWidth"></a>5.1.2.48.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i47_outputColor"></a>5.1.2.48.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i47_format"></a>5.1.2.48.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Power Adapter > format`

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/poweradapterFormat |

**Description:** Output format of the module `PowerAdapter`. See Wiki for formatting syntax
    1. {watts}: Power adapter watts
    2. {name}: Power adapter name
    3. {manufacturer}: Power adapter manufacturer
    4. {model}: Power adapter model
    5. {description}: Power adapter description
    6. {serial}: Power adapter serial number

##### <a name="modules_items_anyOf_i1_oneOf_i48"></a>5.1.2.49. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes`

**Title:** Processes

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                             |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i48_type )               | No      | const            | No         | -                                                                    | Count running processes                                                                                       |
| - [key](#modules_items_anyOf_i1_oneOf_i48_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                             |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i48_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                             |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i48_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                   |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i48_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                    |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i48_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                        |
| - [format](#modules_items_anyOf_i1_oneOf_i48_format )           | No      | string           | No         | In #/$defs/processesFormat                                           | Output format of the module \`Processes\`. See Wiki for formatting syntax<br />    1. {result}: Process count |

###### <a name="modules_items_anyOf_i1_oneOf_i48_type"></a>5.1.2.49.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Count running processes

Specific value: `"processes"`

###### <a name="modules_items_anyOf_i1_oneOf_i48_key"></a>5.1.2.49.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i48_keyColor"></a>5.1.2.49.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i48_keyIcon"></a>5.1.2.49.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i48_keyWidth"></a>5.1.2.49.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i48_outputColor"></a>5.1.2.49.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i48_format"></a>5.1.2.49.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Processes > format`

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | No                      |
| **Defined in** | #/$defs/processesFormat |

**Description:** Output format of the module `Processes`. See Wiki for formatting syntax
    1. {result}: Process count

##### <a name="modules_items_anyOf_i1_oneOf_i49"></a>5.1.2.50. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP`

**Title:** Public IP

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                             |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i49_type )               | No      | const            | No         | -                                                                    | Print your public IP address, etc                                                                                                             |
| - [url](#modules_items_anyOf_i1_oneOf_i49_url )                 | No      | string           | No         | -                                                                    | The URL of public IP detection server to be used. Only HTTP protocol is supported                                                             |
| - [timeout](#modules_items_anyOf_i1_oneOf_i49_timeout )         | No      | integer          | No         | -                                                                    | Time in milliseconds to wait for the public ip server to respond                                                                              |
| - [ipv6](#modules_items_anyOf_i1_oneOf_i49_ipv6 )               | No      | boolean          | No         | -                                                                    | Whether to use IPv6 for public IP detection server                                                                                            |
| - [key](#modules_items_anyOf_i1_oneOf_i49_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                             |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i49_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                             |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i49_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                   |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i49_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                    |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i49_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                        |
| - [format](#modules_items_anyOf_i1_oneOf_i49_format )           | No      | string           | No         | In #/$defs/publicipFormat                                            | Output format of the module \`PublicIp\`. See Wiki for formatting syntax<br />    1. {ip}: Public IP address<br />    2. {location}: Location |

###### <a name="modules_items_anyOf_i1_oneOf_i49_type"></a>5.1.2.50.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print your public IP address, etc

Specific value: `"publicip"`

###### <a name="modules_items_anyOf_i1_oneOf_i49_url"></a>5.1.2.50.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > url`

|              |                         |
| ------------ | ----------------------- |
| **Type**     | `string`                |
| **Required** | No                      |
| **Format**   | `url`                   |
| **Default**  | `"http://ipinfo.io/ip"` |

**Description:** The URL of public IP detection server to be used. Only HTTP protocol is supported

###### <a name="modules_items_anyOf_i1_oneOf_i49_timeout"></a>5.1.2.50.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > timeout`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `integer`        |
| **Required** | No               |
| **Default**  | `"disabled (0)"` |

**Description:** Time in milliseconds to wait for the public ip server to respond

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="modules_items_anyOf_i1_oneOf_i49_ipv6"></a>5.1.2.50.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > ipv6`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Whether to use IPv6 for public IP detection server

###### <a name="modules_items_anyOf_i1_oneOf_i49_key"></a>5.1.2.50.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i49_keyColor"></a>5.1.2.50.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i49_keyIcon"></a>5.1.2.50.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i49_keyWidth"></a>5.1.2.50.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i49_outputColor"></a>5.1.2.50.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i49_format"></a>5.1.2.50.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Public IP > format`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/publicipFormat |

**Description:** Output format of the module `PublicIp`. See Wiki for formatting syntax
    1. {ip}: Public IP address
    2. {location}: Location

##### <a name="modules_items_anyOf_i1_oneOf_i50"></a>5.1.2.51. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator`

**Title:** Separator

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                         |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i50_type )               | No      | const            | No         | -                                                                    | Print a separator line                                    |
| - [string](#modules_items_anyOf_i1_oneOf_i50_string )           | No      | string           | No         | -                                                                    | Set the string to be printed by the separator line        |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i50_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Set the color of the separator line                       |
| - [length](#modules_items_anyOf_i1_oneOf_i50_length )           | No      | integer          | No         | -                                                                    | Set the length of the separator line, or 0 to auto-detect |

###### <a name="modules_items_anyOf_i1_oneOf_i50_type"></a>5.1.2.51.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print a separator line

Specific value: `"separator"`

###### <a name="modules_items_anyOf_i1_oneOf_i50_string"></a>5.1.2.51.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > string`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Default**  | `"-"`    |

**Description:** Set the string to be printed by the separator line

###### <a name="modules_items_anyOf_i1_oneOf_i50_outputColor"></a>5.1.2.51.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Set the color of the separator line

###### <a name="modules_items_anyOf_i1_oneOf_i50_length"></a>5.1.2.51.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Separator > length`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |
| **Default**  | `0`       |

**Description:** Set the length of the separator line, or 0 to auto-detect

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

##### <a name="modules_items_anyOf_i1_oneOf_i51"></a>5.1.2.52. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell`

**Title:** Shell

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i51_type )               | No      | const            | No         | -                                                                    | Print current shell name and version                                                                                                                                                                                                                                                                                                                                                                                                               |
| - [key](#modules_items_anyOf_i1_oneOf_i51_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i51_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i51_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i51_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i51_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i51_format )           | No      | string           | No         | In #/$defs/shellFormat                                               | Output format of the module \`Shell\`. See Wiki for formatting syntax<br />    1. {process-name}: Shell process name<br />    2. {exe}: The first argument of the command line when running the shell<br />    3. {exe-name}: Shell base name of arg0<br />    4. {version}: Shell version<br />    5. {pid}: Shell pid<br />    6. {pretty-name}: Shell pretty name<br />    7. {exe-path}: Shell full exe path<br />    8. {tty}: Shell tty used |

###### <a name="modules_items_anyOf_i1_oneOf_i51_type"></a>5.1.2.52.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current shell name and version

Specific value: `"shell"`

###### <a name="modules_items_anyOf_i1_oneOf_i51_key"></a>5.1.2.52.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i51_keyColor"></a>5.1.2.52.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i51_keyIcon"></a>5.1.2.52.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i51_keyWidth"></a>5.1.2.52.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i51_outputColor"></a>5.1.2.52.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i51_format"></a>5.1.2.52.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Shell > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/shellFormat |

**Description:** Output format of the module `Shell`. See Wiki for formatting syntax
    1. {process-name}: Shell process name
    2. {exe}: The first argument of the command line when running the shell
    3. {exe-name}: Shell base name of arg0
    4. {version}: Shell version
    5. {pid}: Shell pid
    6. {pretty-name}: Shell pretty name
    7. {exe-path}: Shell full exe path
    8. {tty}: Shell tty used

##### <a name="modules_items_anyOf_i1_oneOf_i52"></a>5.1.2.53. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound`

**Title:** Sound

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i52_type )               | No      | const            | No         | -                                                                    | Print sound devices, volume, etc                                                                                                                                                                                                                                                                                                                                 |
| - [soundType](#modules_items_anyOf_i1_oneOf_i52_soundType )     | No      | enum (of string) | No         | -                                                                    | Set what type of sound devices should be printed                                                                                                                                                                                                                                                                                                                 |
| - [percent](#modules_items_anyOf_i1_oneOf_i52_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                 |
| - [key](#modules_items_anyOf_i1_oneOf_i52_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i52_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i52_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                      |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i52_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                       |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i52_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                           |
| - [format](#modules_items_anyOf_i1_oneOf_i52_format )           | No      | string           | No         | In #/$defs/soundFormat                                               | Output format of the module \`Sound\`. See Wiki for formatting syntax<br />    1. {is-main}: Is main sound device<br />    2. {name}: Device name<br />    3. {volume-percentage}: Volume (in percentage num)<br />    4. {identifier}: Identifier<br />    5. {volume-percentage-bar}: Volume (in percentage bar)<br />    6. {platform-api}: Platform API used |

###### <a name="modules_items_anyOf_i1_oneOf_i52_type"></a>5.1.2.53.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print sound devices, volume, etc

Specific value: `"sound"`

###### <a name="modules_items_anyOf_i1_oneOf_i52_soundType"></a>5.1.2.53.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > soundType`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |
| **Default**  | `"main"`           |

**Description:** Set what type of sound devices should be printed

Must be one of:
* "main"
* "active"
* "all"

###### <a name="modules_items_anyOf_i1_oneOf_i52_percent"></a>5.1.2.53.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i52_key"></a>5.1.2.53.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i52_keyColor"></a>5.1.2.53.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i52_keyIcon"></a>5.1.2.53.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i52_keyWidth"></a>5.1.2.53.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i52_outputColor"></a>5.1.2.53.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i52_format"></a>5.1.2.53.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Sound > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/soundFormat |

**Description:** Output format of the module `Sound`. See Wiki for formatting syntax
    1. {is-main}: Is main sound device
    2. {name}: Device name
    3. {volume-percentage}: Volume (in percentage num)
    4. {identifier}: Identifier
    5. {volume-percentage-bar}: Volume (in percentage bar)
    6. {platform-api}: Platform API used

##### <a name="modules_items_anyOf_i1_oneOf_i53"></a>5.1.2.54. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap`

**Title:** Swap

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i53_type )               | No      | const            | No         | -                                                                    | Print swap (paging file) space usage                                                                                                                                                                                                   |
| - [percent](#modules_items_anyOf_i1_oneOf_i53_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                       |
| - [key](#modules_items_anyOf_i1_oneOf_i53_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i53_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i53_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i53_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i53_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i53_format )           | No      | string           | No         | In #/$defs/swapFormat                                                | Output format of the module \`Swap\`. See Wiki for formatting syntax<br />    1. {used}: Used size<br />    2. {total}: Total size<br />    3. {percentage}: Percentage used (num)<br />    4. {percentage-bar}: Percentage used (bar) |

###### <a name="modules_items_anyOf_i1_oneOf_i53_type"></a>5.1.2.54.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print swap (paging file) space usage

Specific value: `"swap"`

###### <a name="modules_items_anyOf_i1_oneOf_i53_percent"></a>5.1.2.54.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i53_key"></a>5.1.2.54.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i53_keyColor"></a>5.1.2.54.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i53_keyIcon"></a>5.1.2.54.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i53_keyWidth"></a>5.1.2.54.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i53_outputColor"></a>5.1.2.54.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i53_format"></a>5.1.2.54.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Swap > format`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/swapFormat |

**Description:** Output format of the module `Swap`. See Wiki for formatting syntax
    1. {used}: Used size
    2. {total}: Total size
    3. {percentage}: Percentage used (num)
    4. {percentage-bar}: Percentage used (bar)

##### <a name="modules_items_anyOf_i1_oneOf_i54"></a>5.1.2.55. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal`

**Title:** Terminal

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i54_type )               | No      | const            | No         | -                                                                    | Print current terminal name and version                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [key](#modules_items_anyOf_i1_oneOf_i54_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i54_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i54_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i54_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i54_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [format](#modules_items_anyOf_i1_oneOf_i54_format )           | No      | string           | No         | In #/$defs/terminalFormat                                            | Output format of the module \`Terminal\`. See Wiki for formatting syntax<br />    1. {process-name}: Terminal process name<br />    2. {exe}: The first argument of the command line when running the terminal<br />    3. {exe-name}: Terminal base name of arg0<br />    4. {pid}: Terminal pid<br />    5. {pretty-name}: Terminal pretty name<br />    6. {version}: Terminal version<br />    7. {exe-path}: Terminal full exe path<br />    8. {tty}: Terminal tty / pts used |

###### <a name="modules_items_anyOf_i1_oneOf_i54_type"></a>5.1.2.55.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current terminal name and version

Specific value: `"terminal"`

###### <a name="modules_items_anyOf_i1_oneOf_i54_key"></a>5.1.2.55.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i54_keyColor"></a>5.1.2.55.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i54_keyIcon"></a>5.1.2.55.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i54_keyWidth"></a>5.1.2.55.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i54_outputColor"></a>5.1.2.55.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i54_format"></a>5.1.2.55.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal > format`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `string`               |
| **Required**   | No                     |
| **Defined in** | #/$defs/terminalFormat |

**Description:** Output format of the module `Terminal`. See Wiki for formatting syntax
    1. {process-name}: Terminal process name
    2. {exe}: The first argument of the command line when running the terminal
    3. {exe-name}: Terminal base name of arg0
    4. {pid}: Terminal pid
    5. {pretty-name}: Terminal pretty name
    6. {version}: Terminal version
    7. {exe-path}: Terminal full exe path
    8. {tty}: Terminal tty / pts used

##### <a name="modules_items_anyOf_i1_oneOf_i55"></a>5.1.2.56. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font`

**Title:** Terminal Font

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                    |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i55_type )               | No      | const            | No         | -                                                                    | Print font name and size used by current terminal                                                                                                                                                                                                    |
| - [key](#modules_items_anyOf_i1_oneOf_i55_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                    |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i55_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                    |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i55_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                          |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i55_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                           |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i55_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                               |
| - [format](#modules_items_anyOf_i1_oneOf_i55_format )           | No      | string           | No         | In #/$defs/terminalfontFormat                                        | Output format of the module \`TerminalFont\`. See Wiki for formatting syntax<br />    1. {combined}: Terminal font combined<br />    2. {name}: Terminal font name<br />    3. {size}: Terminal font size<br />    4. {styles}: Terminal font styles |

###### <a name="modules_items_anyOf_i1_oneOf_i55_type"></a>5.1.2.56.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print font name and size used by current terminal

Specific value: `"terminalfont"`

###### <a name="modules_items_anyOf_i1_oneOf_i55_key"></a>5.1.2.56.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i55_keyColor"></a>5.1.2.56.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i55_keyIcon"></a>5.1.2.56.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i55_keyWidth"></a>5.1.2.56.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i55_outputColor"></a>5.1.2.56.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i55_format"></a>5.1.2.56.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Font > format`

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/terminalfontFormat |

**Description:** Output format of the module `TerminalFont`. See Wiki for formatting syntax
    1. {combined}: Terminal font combined
    2. {name}: Terminal font name
    3. {size}: Terminal font size
    4. {styles}: Terminal font styles

##### <a name="modules_items_anyOf_i1_oneOf_i56"></a>5.1.2.57. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size`

**Title:** Terminal Size

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                        |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i56_type )               | No      | const            | No         | -                                                                    | Print current terminal size                                                                                                                                                                                                                              |
| - [key](#modules_items_anyOf_i1_oneOf_i56_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                        |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i56_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                        |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i56_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                              |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i56_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                               |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i56_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                   |
| - [format](#modules_items_anyOf_i1_oneOf_i56_format )           | No      | string           | No         | In #/$defs/terminalsizeFormat                                        | Output format of the module \`TerminalSize\`. See Wiki for formatting syntax<br />    1. {rows}: Terminal rows<br />    2. {columns}: Terminal columns<br />    3. {width}: Terminal width (in pixels)<br />    4. {height}: Terminal height (in pixels) |

###### <a name="modules_items_anyOf_i1_oneOf_i56_type"></a>5.1.2.57.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current terminal size

Specific value: `"terminalsize"`

###### <a name="modules_items_anyOf_i1_oneOf_i56_key"></a>5.1.2.57.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i56_keyColor"></a>5.1.2.57.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i56_keyIcon"></a>5.1.2.57.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i56_keyWidth"></a>5.1.2.57.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i56_outputColor"></a>5.1.2.57.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i56_format"></a>5.1.2.57.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Size > format`

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `string`                   |
| **Required**   | No                         |
| **Defined in** | #/$defs/terminalsizeFormat |

**Description:** Output format of the module `TerminalSize`. See Wiki for formatting syntax
    1. {rows}: Terminal rows
    2. {columns}: Terminal columns
    3. {width}: Terminal width (in pixels)
    4. {height}: Terminal height (in pixels)

##### <a name="modules_items_anyOf_i1_oneOf_i57"></a>5.1.2.58. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme`

**Title:** Terminal Theme

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i57_type )               | No      | const            | No         | -                                                                    | Print current terminal theme (foreground and background colors)                                                                                                                                                                                                                                                 |
| - [key](#modules_items_anyOf_i1_oneOf_i57_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                               |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i57_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                               |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i57_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                     |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i57_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                      |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i57_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                          |
| - [format](#modules_items_anyOf_i1_oneOf_i57_format )           | No      | string           | No         | In #/$defs/terminalthemeFormat                                       | Output format of the module \`TerminalTheme\`. See Wiki for formatting syntax<br />    1. {fg-color}: Terminal foreground color<br />    2. {fg-type}: Terminal foreground type (Dark / Light)<br />    3. {bg-color}: Terminal background color<br />    4. {bg-type}: Terminal background type (Dark / Light) |

###### <a name="modules_items_anyOf_i1_oneOf_i57_type"></a>5.1.2.58.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current terminal theme (foreground and background colors)

Specific value: `"terminaltheme"`

###### <a name="modules_items_anyOf_i1_oneOf_i57_key"></a>5.1.2.58.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i57_keyColor"></a>5.1.2.58.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i57_keyIcon"></a>5.1.2.58.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i57_keyWidth"></a>5.1.2.58.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i57_outputColor"></a>5.1.2.58.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i57_format"></a>5.1.2.58.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Terminal Theme > format`

|                |                             |
| -------------- | --------------------------- |
| **Type**       | `string`                    |
| **Required**   | No                          |
| **Defined in** | #/$defs/terminalthemeFormat |

**Description:** Output format of the module `TerminalTheme`. See Wiki for formatting syntax
    1. {fg-color}: Terminal foreground color
    2. {fg-type}: Terminal foreground type (Dark / Light)
    3. {bg-color}: Terminal background color
    4. {bg-type}: Terminal background type (Dark / Light)

##### <a name="modules_items_anyOf_i1_oneOf_i58"></a>5.1.2.59. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme`

**Title:** Theme

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                           |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i58_type )               | No      | const            | No         | -                                                                    | Print current theme of desktop environment                                                                                                  |
| - [key](#modules_items_anyOf_i1_oneOf_i58_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                           |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i58_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                           |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i58_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                 |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i58_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                  |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i58_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                      |
| - [format](#modules_items_anyOf_i1_oneOf_i58_format )           | No      | string           | No         | In #/$defs/themeFormat                                               | Output format of the module \`Theme\`. See Wiki for formatting syntax<br />    1. {theme1}: Theme part 1<br />    2. {theme2}: Theme part 2 |

###### <a name="modules_items_anyOf_i1_oneOf_i58_type"></a>5.1.2.59.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current theme of desktop environment

Specific value: `"theme"`

###### <a name="modules_items_anyOf_i1_oneOf_i58_key"></a>5.1.2.59.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i58_keyColor"></a>5.1.2.59.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i58_keyIcon"></a>5.1.2.59.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i58_keyWidth"></a>5.1.2.59.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i58_outputColor"></a>5.1.2.59.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i58_format"></a>5.1.2.59.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Theme > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/themeFormat |

**Description:** Output format of the module `Theme`. See Wiki for formatting syntax
    1. {theme1}: Theme part 1
    2. {theme2}: Theme part 2

##### <a name="modules_items_anyOf_i1_oneOf_i59"></a>5.1.2.60. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title`

**Title:** Title

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i59_type )               | No      | const            | No         | -                                                                    | Print title, which contains your user name, hostname                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [fqdn](#modules_items_anyOf_i1_oneOf_i59_fqdn )               | No      | boolean          | No         | -                                                                    | Set if the title should use fully qualified domain name                                                                                                                                                                                                                                                                                                                                                                                                    |
| - [color](#modules_items_anyOf_i1_oneOf_i59_color )             | No      | object           | No         | -                                                                    | Set colors of the different part of title                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [key](#modules_items_anyOf_i1_oneOf_i59_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i59_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                          |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i59_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i59_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i59_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                     |
| - [format](#modules_items_anyOf_i1_oneOf_i59_format )           | No      | string           | No         | In #/$defs/titleFormat                                               | Output format of the module \`Title\`. See Wiki for formatting syntax<br />    1. {user-name}: User name<br />    2. {host-name}: Host name<br />    3. {home-dir}: Home directory<br />    4. {exe-path}: Executable path of current process<br />    5. {user-shell}: User's default shell<br />    6. {user-name-colored}: User name (colored)<br />    7. {at-symbol-colored}: @ symbol (colored)<br />    8. {host-name-colored}: Host name (colored) |

###### <a name="modules_items_anyOf_i1_oneOf_i59_type"></a>5.1.2.60.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print title, which contains your user name, hostname

Specific value: `"title"`

###### <a name="modules_items_anyOf_i1_oneOf_i59_fqdn"></a>5.1.2.60.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > fqdn`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if the title should use fully qualified domain name

###### <a name="modules_items_anyOf_i1_oneOf_i59_color"></a>5.1.2.60.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color`

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

**Description:** Set colors of the different part of title

| Property                                                | Pattern | Type             | Deprecated | Definition                           | Title/Description                       |
| ------------------------------------------------------- | ------- | ---------------- | ---------- | ------------------------------------ | --------------------------------------- |
| - [user](#modules_items_anyOf_i1_oneOf_i59_color_user ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set color of the user name (left part)  |
| - [at](#modules_items_anyOf_i1_oneOf_i59_color_at )     | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set color of the @ symbol (middle part) |
| - [host](#modules_items_anyOf_i1_oneOf_i59_color_host ) | No      | enum (of string) | No         | Same as [1](#logo_oneOf_i2_color_1 ) | Set color of the host name (right part) |

###### <a name="modules_items_anyOf_i1_oneOf_i59_color_user"></a>5.1.2.60.3.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > user`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set color of the user name (left part)

###### <a name="modules_items_anyOf_i1_oneOf_i59_color_at"></a>5.1.2.60.3.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > at`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set color of the @ symbol (middle part)

###### <a name="modules_items_anyOf_i1_oneOf_i59_color_host"></a>5.1.2.60.3.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > color > host`

|                        |                             |
| ---------------------- | --------------------------- |
| **Type**               | `enum (of string)`          |
| **Required**           | No                          |
| **Same definition as** | [1](#logo_oneOf_i2_color_1) |

**Description:** Set color of the host name (right part)

###### <a name="modules_items_anyOf_i1_oneOf_i59_key"></a>5.1.2.60.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i59_keyColor"></a>5.1.2.60.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i59_keyIcon"></a>5.1.2.60.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i59_keyWidth"></a>5.1.2.60.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i59_outputColor"></a>5.1.2.60.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i59_format"></a>5.1.2.60.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Title > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/titleFormat |

**Description:** Output format of the module `Title`. See Wiki for formatting syntax
    1. {user-name}: User name
    2. {host-name}: Host name
    3. {home-dir}: Home directory
    4. {exe-path}: Executable path of current process
    5. {user-shell}: User's default shell
    6. {user-name-colored}: User name (colored)
    7. {at-symbol-colored}: @ symbol (colored)
    8. {host-name-colored}: Host name (colored)

##### <a name="modules_items_anyOf_i1_oneOf_i60"></a>5.1.2.61. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM`

**Title:** TPM

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i60_type )               | No      | const            | No         | -                                                                    | Print info of Trusted Platform Module (TPM) Security Device                                                                                                      |
| - [key](#modules_items_anyOf_i1_oneOf_i60_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i60_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i60_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                      |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i60_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                       |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i60_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                           |
| - [format](#modules_items_anyOf_i1_oneOf_i60_format )           | No      | string           | No         | In #/$defs/tpmFormat                                                 | Output format of the module \`TPM\`. See Wiki for formatting syntax<br />    1. {version}: TPM device version<br />    2. {description}: TPM general description |

###### <a name="modules_items_anyOf_i1_oneOf_i60_type"></a>5.1.2.61.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print info of Trusted Platform Module (TPM) Security Device

Specific value: `"tpm"`

###### <a name="modules_items_anyOf_i1_oneOf_i60_key"></a>5.1.2.61.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i60_keyColor"></a>5.1.2.61.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i60_keyIcon"></a>5.1.2.61.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i60_keyWidth"></a>5.1.2.61.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i60_outputColor"></a>5.1.2.61.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i60_format"></a>5.1.2.61.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > TPM > format`

|                |                   |
| -------------- | ----------------- |
| **Type**       | `string`          |
| **Required**   | No                |
| **Defined in** | #/$defs/tpmFormat |

**Description:** Output format of the module `TPM`. See Wiki for formatting syntax
    1. {version}: TPM device version
    2. {description}: TPM general description

##### <a name="modules_items_anyOf_i1_oneOf_i61"></a>5.1.2.62. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users`

**Title:** Users

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i61_type )               | No      | const            | No         | -                                                                    | Print users currently logged in                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [compact](#modules_items_anyOf_i1_oneOf_i61_compact )         | No      | boolean          | No         | -                                                                    | Show all active users in one line                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [myselfOnly](#modules_items_anyOf_i1_oneOf_i61_myselfOnly )   | No      | boolean          | No         | -                                                                    | Show only the current user                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [key](#modules_items_anyOf_i1_oneOf_i61_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i61_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i61_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i61_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i61_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - [format](#modules_items_anyOf_i1_oneOf_i61_format )           | No      | string           | No         | In #/$defs/usersFormat                                               | Output format of the module \`Users\`. See Wiki for formatting syntax<br />    1. {name}: User name<br />    2. {host-name}: Host name<br />    3. {session}: Session name<br />    4. {client-ip}: Client IP<br />    5. {login-time}: Login Time in local timezone<br />    6. {days}: Days after login<br />    7. {hours}: Hours after login<br />    8. {minutes}: Minutes after login<br />    9. {seconds}: Seconds after login<br />    10. {milliseconds}: Milliseconds after login |

###### <a name="modules_items_anyOf_i1_oneOf_i61_type"></a>5.1.2.62.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print users currently logged in

Specific value: `"users"`

###### <a name="modules_items_anyOf_i1_oneOf_i61_compact"></a>5.1.2.62.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > compact`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show all active users in one line

###### <a name="modules_items_anyOf_i1_oneOf_i61_myselfOnly"></a>5.1.2.62.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > myselfOnly`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Show only the current user

###### <a name="modules_items_anyOf_i1_oneOf_i61_key"></a>5.1.2.62.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i61_keyColor"></a>5.1.2.62.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i61_keyIcon"></a>5.1.2.62.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i61_keyWidth"></a>5.1.2.62.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i61_outputColor"></a>5.1.2.62.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i61_format"></a>5.1.2.62.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Users > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/usersFormat |

**Description:** Output format of the module `Users`. See Wiki for formatting syntax
    1. {name}: User name
    2. {host-name}: Host name
    3. {session}: Session name
    4. {client-ip}: Client IP
    5. {login-time}: Login Time in local timezone
    6. {days}: Days after login
    7. {hours}: Hours after login
    8. {minutes}: Minutes after login
    9. {seconds}: Seconds after login
    10. {milliseconds}: Milliseconds after login

##### <a name="modules_items_anyOf_i1_oneOf_i62"></a>5.1.2.63. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime`

**Title:** Uptime

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i62_type )               | No      | const            | No         | -                                                                    | Print how long system has been running                                                                                                                                                                                                                                                 |
| - [key](#modules_items_anyOf_i1_oneOf_i62_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i62_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i62_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i62_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i62_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i62_format )           | No      | string           | No         | In #/$defs/uptimeFormat                                              | Output format of the module \`Uptime\`. See Wiki for formatting syntax<br />    1. {days}: Days<br />    2. {hours}: Hours<br />    3. {minutes}: Minutes<br />    4. {seconds}: Seconds<br />    5. {milliseconds}: Milliseconds<br />    6. {boot-time}: Boot time in local timezone |

###### <a name="modules_items_anyOf_i1_oneOf_i62_type"></a>5.1.2.63.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print how long system has been running

Specific value: `"uptime"`

###### <a name="modules_items_anyOf_i1_oneOf_i62_key"></a>5.1.2.63.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i62_keyColor"></a>5.1.2.63.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i62_keyIcon"></a>5.1.2.63.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i62_keyWidth"></a>5.1.2.63.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i62_outputColor"></a>5.1.2.63.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i62_format"></a>5.1.2.63.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Uptime > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/uptimeFormat |

**Description:** Output format of the module `Uptime`. See Wiki for formatting syntax
    1. {days}: Days
    2. {hours}: Hours
    3. {minutes}: Minutes
    4. {seconds}: Seconds
    5. {milliseconds}: Milliseconds
    6. {boot-time}: Boot time in local timezone

##### <a name="modules_items_anyOf_i1_oneOf_i63"></a>5.1.2.64. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version`

**Title:** Version

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i63_type )               | No      | const            | No         | -                                                                    | Print Fastfetch version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - [key](#modules_items_anyOf_i1_oneOf_i63_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i63_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i63_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i63_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i63_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [format](#modules_items_anyOf_i1_oneOf_i63_format )           | No      | string           | No         | In #/$defs/versionFormat                                             | Output format of the module \`Version\`. See Wiki for formatting syntax<br />    1. {name}: Project name<br />    2. {version}: Version<br />    3. {version-tweak}: Version tweak<br />    4. {build-type}: Build type (debug or release)<br />    5. {sysname}: System name<br />    6. {arch}: Architecture<br />    7. {cmake-built-type}: CMake build type when compiling (Debug, Release, RelWithDebInfo, MinSizeRel)<br />    8. {compile-time}: Date time when compiling<br />    9. {compiler}: Compiler used when compiling<br />    10. {libc}: Libc used when compiling |

###### <a name="modules_items_anyOf_i1_oneOf_i63_type"></a>5.1.2.64.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print Fastfetch version

Specific value: `"version"`

###### <a name="modules_items_anyOf_i1_oneOf_i63_key"></a>5.1.2.64.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i63_keyColor"></a>5.1.2.64.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i63_keyIcon"></a>5.1.2.64.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i63_keyWidth"></a>5.1.2.64.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i63_outputColor"></a>5.1.2.64.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i63_format"></a>5.1.2.64.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Version > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/versionFormat |

**Description:** Output format of the module `Version`. See Wiki for formatting syntax
    1. {name}: Project name
    2. {version}: Version
    3. {version-tweak}: Version tweak
    4. {build-type}: Build type (debug or release)
    5. {sysname}: System name
    6. {arch}: Architecture
    7. {cmake-built-type}: CMake build type when compiling (Debug, Release, RelWithDebInfo, MinSizeRel)
    8. {compile-time}: Date time when compiling
    9. {compiler}: Compiler used when compiling
    10. {libc}: Libc used when compiling

##### <a name="modules_items_anyOf_i1_oneOf_i64"></a>5.1.2.65. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan`

**Title:** Vulkan

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                       |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i64_type )               | No      | const            | No         | -                                                                    | Print highest Vulkan version supported by the GPU                                                                                                                                                                                                       |
| - [key](#modules_items_anyOf_i1_oneOf_i64_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                       |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i64_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                       |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i64_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                             |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i64_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                              |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i64_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                  |
| - [format](#modules_items_anyOf_i1_oneOf_i64_format )           | No      | string           | No         | In #/$defs/vulkanFormat                                              | Output format of the module \`Vulkan\`. See Wiki for formatting syntax<br />    1. {driver}: Driver name<br />    2. {api-version}: API version<br />    3. {conformance-version}: Conformance version<br />    4. {instance-version}: Instance version |

###### <a name="modules_items_anyOf_i1_oneOf_i64_type"></a>5.1.2.65.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print highest Vulkan version supported by the GPU

Specific value: `"vulkan"`

###### <a name="modules_items_anyOf_i1_oneOf_i64_key"></a>5.1.2.65.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i64_keyColor"></a>5.1.2.65.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i64_keyIcon"></a>5.1.2.65.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i64_keyWidth"></a>5.1.2.65.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i64_outputColor"></a>5.1.2.65.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i64_format"></a>5.1.2.65.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Vulkan > format`

|                |                      |
| -------------- | -------------------- |
| **Type**       | `string`             |
| **Required**   | No                   |
| **Defined in** | #/$defs/vulkanFormat |

**Description:** Output format of the module `Vulkan`. See Wiki for formatting syntax
    1. {driver}: Driver name
    2. {api-version}: API version
    3. {conformance-version}: Conformance version
    4. {instance-version}: Instance version

##### <a name="modules_items_anyOf_i1_oneOf_i65"></a>5.1.2.66. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper`

**Title:** Wallpaper

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                               |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i65_type )               | No      | const            | No         | -                                                                    | Print image file path of current wallpaper                                                                                                      |
| - [key](#modules_items_anyOf_i1_oneOf_i65_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                               |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i65_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                               |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i65_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                     |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i65_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                      |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i65_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                          |
| - [format](#modules_items_anyOf_i1_oneOf_i65_format )           | No      | string           | No         | In #/$defs/wallpaperFormat                                           | Output format of the module \`Wallpaper\`. See Wiki for formatting syntax<br />    1. {file-name}: File name<br />    2. {full-path}: Full path |

###### <a name="modules_items_anyOf_i1_oneOf_i65_type"></a>5.1.2.66.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print image file path of current wallpaper

Specific value: `"wallpaper"`

###### <a name="modules_items_anyOf_i1_oneOf_i65_key"></a>5.1.2.66.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i65_keyColor"></a>5.1.2.66.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i65_keyIcon"></a>5.1.2.66.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i65_keyWidth"></a>5.1.2.66.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i65_outputColor"></a>5.1.2.66.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i65_format"></a>5.1.2.66.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wallpaper > format`

|                |                         |
| -------------- | ----------------------- |
| **Type**       | `string`                |
| **Required**   | No                      |
| **Defined in** | #/$defs/wallpaperFormat |

**Description:** Output format of the module `Wallpaper`. See Wiki for formatting syntax
    1. {file-name}: File name
    2. {full-path}: Full path

##### <a name="modules_items_anyOf_i1_oneOf_i66"></a>5.1.2.67. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather`

**Title:** Weather

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                          | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                            |
| ----------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i66_type )                 | No      | const            | No         | -                                                                    | Print weather information                                                                                    |
| - [location](#modules_items_anyOf_i1_oneOf_i66_location )         | No      | string           | No         | -                                                                    | The location to display                                                                                      |
| - [timeout](#modules_items_anyOf_i1_oneOf_i66_timeout )           | No      | integer          | No         | -                                                                    | Time in milliseconds to wait for the weather server to respond                                               |
| - [outputFormat](#modules_items_anyOf_i1_oneOf_i66_outputFormat ) | No      | string           | No         | -                                                                    | The output weather format to be used (must be URI encoded)                                                   |
| - [key](#modules_items_anyOf_i1_oneOf_i66_key )                   | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                            |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i66_keyColor )         | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                            |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i66_keyIcon )           | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                  |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i66_keyWidth )         | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                   |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i66_outputColor )   | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                       |
| - [format](#modules_items_anyOf_i1_oneOf_i66_format )             | No      | string           | No         | In #/$defs/weatherFormat                                             | Output format of the module \`Weather\`. See Wiki for formatting syntax<br />    1. {result}: Weather result |

###### <a name="modules_items_anyOf_i1_oneOf_i66_type"></a>5.1.2.67.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print weather information

Specific value: `"weather"`

###### <a name="modules_items_anyOf_i1_oneOf_i66_location"></a>5.1.2.67.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > location`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The location to display

###### <a name="modules_items_anyOf_i1_oneOf_i66_timeout"></a>5.1.2.67.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > timeout`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `integer`        |
| **Required** | No               |
| **Default**  | `"disabled (0)"` |

**Description:** Time in milliseconds to wait for the weather server to respond

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="modules_items_anyOf_i1_oneOf_i66_outputFormat"></a>5.1.2.67.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputFormat`

|              |                  |
| ------------ | ---------------- |
| **Type**     | `string`         |
| **Required** | No               |
| **Default**  | `"%t+-+%C+(%l)"` |

**Description:** The output weather format to be used (must be URI encoded)

###### <a name="modules_items_anyOf_i1_oneOf_i66_key"></a>5.1.2.67.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i66_keyColor"></a>5.1.2.67.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i66_keyIcon"></a>5.1.2.67.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i66_keyWidth"></a>5.1.2.67.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i66_outputColor"></a>5.1.2.67.9. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i66_format"></a>5.1.2.67.10. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Weather > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/weatherFormat |

**Description:** Output format of the module `Weather`. See Wiki for formatting syntax
    1. {result}: Weather result

##### <a name="modules_items_anyOf_i1_oneOf_i67"></a>5.1.2.68. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi`

**Title:** Wi-Fi

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i67_type )               | No      | const            | No         | -                                                                    | Print connected Wi-Fi info (SSID, connection and security protocol)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [key](#modules_items_anyOf_i1_oneOf_i67_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i67_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i67_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i67_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i67_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - [format](#modules_items_anyOf_i1_oneOf_i67_format )           | No      | string           | No         | In #/$defs/wifiFormat                                                | Output format of the module \`Wifi\`. See Wiki for formatting syntax<br />    1. {inf-desc}: Interface description<br />    2. {inf-status}: Interface status<br />    3. {status}: Connection status<br />    4. {ssid}: Connection SSID<br />    5. {bssid}: Connection BSSID<br />    6. {protocol}: Connection protocol<br />    7. {signal-quality}: Connection signal quality (percentage num)<br />    8. {rx-rate}: Connection RX rate<br />    9. {tx-rate}: Connection TX rate<br />    10. {security}: Connection Security algorithm<br />    11. {signal-quality-bar}: Connection signal quality (percentage bar)<br />    12. {channel}: Connection channel number<br />    13. {band}: Connection channel band in GHz |

###### <a name="modules_items_anyOf_i1_oneOf_i67_type"></a>5.1.2.68.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print connected Wi-Fi info (SSID, connection and security protocol)

Specific value: `"wifi"`

###### <a name="modules_items_anyOf_i1_oneOf_i67_key"></a>5.1.2.68.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i67_keyColor"></a>5.1.2.68.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i67_keyIcon"></a>5.1.2.68.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i67_keyWidth"></a>5.1.2.68.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i67_outputColor"></a>5.1.2.68.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i67_format"></a>5.1.2.68.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Wi-Fi > format`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `string`           |
| **Required**   | No                 |
| **Defined in** | #/$defs/wifiFormat |

**Description:** Output format of the module `Wifi`. See Wiki for formatting syntax
    1. {inf-desc}: Interface description
    2. {inf-status}: Interface status
    3. {status}: Connection status
    4. {ssid}: Connection SSID
    5. {bssid}: Connection BSSID
    6. {protocol}: Connection protocol
    7. {signal-quality}: Connection signal quality (percentage num)
    8. {rx-rate}: Connection RX rate
    9. {tx-rate}: Connection TX rate
    10. {security}: Connection Security algorithm
    11. {signal-quality-bar}: Connection signal quality (percentage bar)
    12. {channel}: Connection channel number
    13. {band}: Connection channel band in GHz

##### <a name="modules_items_anyOf_i1_oneOf_i68"></a>5.1.2.69. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager`

**Title:** Window Manager

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                          | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i68_type )                 | No      | const            | No         | -                                                                    | Print window manager name and version                                                                                                                                                                                                                                              |
| - [detectPlugin](#modules_items_anyOf_i1_oneOf_i68_detectPlugin ) | No      | boolean          | No         | -                                                                    | Set if window manager plugin should be detected on supported platforms                                                                                                                                                                                                             |
| - [key](#modules_items_anyOf_i1_oneOf_i68_key )                   | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                  |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i68_keyColor )         | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                  |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i68_keyIcon )           | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                        |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i68_keyWidth )         | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                         |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i68_outputColor )   | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                             |
| - [format](#modules_items_anyOf_i1_oneOf_i68_format )             | No      | string           | No         | In #/$defs/wmFormat                                                  | Output format of the module \`WM\`. See Wiki for formatting syntax<br />    1. {process-name}: WM process name<br />    2. {pretty-name}: WM pretty name<br />    3. {protocol-name}: WM protocol name<br />    4. {plugin-name}: WM plugin name<br />    5. {version}: WM version |

###### <a name="modules_items_anyOf_i1_oneOf_i68_type"></a>5.1.2.69.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print window manager name and version

Specific value: `"wm"`

###### <a name="modules_items_anyOf_i1_oneOf_i68_detectPlugin"></a>5.1.2.69.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > detectPlugin`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |
| **Default**  | `false`   |

**Description:** Set if window manager plugin should be detected on supported platforms

###### <a name="modules_items_anyOf_i1_oneOf_i68_key"></a>5.1.2.69.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i68_keyColor"></a>5.1.2.69.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i68_keyIcon"></a>5.1.2.69.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i68_keyWidth"></a>5.1.2.69.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i68_outputColor"></a>5.1.2.69.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i68_format"></a>5.1.2.69.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Window Manager > format`

|                |                  |
| -------------- | ---------------- |
| **Type**       | `string`         |
| **Required**   | No               |
| **Defined in** | #/$defs/wmFormat |

**Description:** Output format of the module `WM`. See Wiki for formatting syntax
    1. {process-name}: WM process name
    2. {pretty-name}: WM pretty name
    3. {protocol-name}: WM protocol name
    4. {plugin-name}: WM plugin name
    5. {version}: WM version

##### <a name="modules_items_anyOf_i1_oneOf_i69"></a>5.1.2.70. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme`

**Title:** WM Theme

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                      |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| - [type](#modules_items_anyOf_i1_oneOf_i69_type )               | No      | const            | No         | -                                                                    | Print current theme of window manager                                                                  |
| - [key](#modules_items_anyOf_i1_oneOf_i69_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                      |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i69_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                      |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i69_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                            |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i69_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                             |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i69_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                 |
| - [format](#modules_items_anyOf_i1_oneOf_i69_format )           | No      | string           | No         | In #/$defs/wmthemeFormat                                             | Output format of the module \`WMTheme\`. See Wiki for formatting syntax<br />    1. {result}: WM theme |

###### <a name="modules_items_anyOf_i1_oneOf_i69_type"></a>5.1.2.70.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print current theme of window manager

Specific value: `"wmtheme"`

###### <a name="modules_items_anyOf_i1_oneOf_i69_key"></a>5.1.2.70.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i69_keyColor"></a>5.1.2.70.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i69_keyIcon"></a>5.1.2.70.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i69_keyWidth"></a>5.1.2.70.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i69_outputColor"></a>5.1.2.70.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i69_format"></a>5.1.2.70.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > WM Theme > format`

|                |                       |
| -------------- | --------------------- |
| **Type**       | `string`              |
| **Required**   | No                    |
| **Defined in** | #/$defs/wmthemeFormat |

**Description:** Output format of the module `WMTheme`. See Wiki for formatting syntax
    1. {result}: WM theme

##### <a name="modules_items_anyOf_i1_oneOf_i70"></a>5.1.2.71. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool`

**Title:** Zpool

|                           |             |
| ------------------------- | ----------- |
| **Type**                  | `object`    |
| **Required**              | No          |
| **Additional properties** | Not allowed |

| Property                                                        | Pattern | Type             | Deprecated | Definition                                                           | Title/Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------- | ------- | ---------------- | ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [type](#modules_items_anyOf_i1_oneOf_i70_type )               | No      | const            | No         | -                                                                    | Print ZFS storage pools                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - [percent](#modules_items_anyOf_i1_oneOf_i70_percent )         | No      | object           | No         | Same as [percent](#modules_items_anyOf_i1_oneOf_i1_percent )         | Thresholds for percentage colors                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - [key](#modules_items_anyOf_i1_oneOf_i70_key )                 | No      | string           | No         | Same as [key](#modules_items_anyOf_i1_oneOf_i1_key )                 | Key of the module                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - [keyColor](#modules_items_anyOf_i1_oneOf_i70_keyColor )       | No      | enum (of string) | No         | Same as [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor )       | Color of the module key. Left empty to use \`display.color.keys\`                                                                                                                                                                                                                                                                                                                                                                                           |
| - [keyIcon](#modules_items_anyOf_i1_oneOf_i70_keyIcon )         | No      | string           | No         | Same as [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon )         | Set the icon to be displayed by \`display.keyType: "icon"\`                                                                                                                                                                                                                                                                                                                                                                                                 |
| - [keyWidth](#modules_items_anyOf_i1_oneOf_i70_keyWidth )       | No      | integer          | No         | Same as [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth )       | Width of the module key. Use 0 to use \`display.keyWidth\`                                                                                                                                                                                                                                                                                                                                                                                                  |
| - [outputColor](#modules_items_anyOf_i1_oneOf_i70_outputColor ) | No      | enum (of string) | No         | Same as [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor ) | Output color of the module. Left empty to use \`display.color.output\`                                                                                                                                                                                                                                                                                                                                                                                      |
| - [format](#modules_items_anyOf_i1_oneOf_i70_format )           | No      | string           | No         | In #/$defs/zpoolFormat                                               | Output format of the module \`Zpool\`. See Wiki for formatting syntax<br />    1. {name}: Zpool name<br />    2. {state}: Zpool state<br />    3. {used}: Size used<br />    4. {total}: Size total<br />    5. {used-percentage}: Size percentage num<br />    6. {fragmentation-percentage}: Fragmentation percentage num<br />    7. {used-percentage-bar}: Size percentage bar<br />    8. {fragmentation-percentage-bar}: Fragmentation percentage bar |

###### <a name="modules_items_anyOf_i1_oneOf_i70_type"></a>5.1.2.71.1. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | No      |

**Description:** Print ZFS storage pools

Specific value: `"zpool"`

###### <a name="modules_items_anyOf_i1_oneOf_i70_percent"></a>5.1.2.71.2. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > percent`

|                           |                                                     |
| ------------------------- | --------------------------------------------------- |
| **Type**                  | `object`                                            |
| **Required**              | No                                                  |
| **Additional properties** | Not allowed                                         |
| **Same definition as**    | [percent](#modules_items_anyOf_i1_oneOf_i1_percent) |

**Description:** Thresholds for percentage colors

###### <a name="modules_items_anyOf_i1_oneOf_i70_key"></a>5.1.2.71.3. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > key`

|                        |                                             |
| ---------------------- | ------------------------------------------- |
| **Type**               | `string`                                    |
| **Required**           | No                                          |
| **Same definition as** | [key](#modules_items_anyOf_i1_oneOf_i1_key) |

**Description:** Key of the module

###### <a name="modules_items_anyOf_i1_oneOf_i70_keyColor"></a>5.1.2.71.4. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyColor`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `enum (of string)`                                    |
| **Required**           | No                                                    |
| **Same definition as** | [keyColor](#modules_items_anyOf_i1_oneOf_i1_keyColor) |

**Description:** Color of the module key. Left empty to use `display.color.keys`

###### <a name="modules_items_anyOf_i1_oneOf_i70_keyIcon"></a>5.1.2.71.5. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyIcon`

|                        |                                                     |
| ---------------------- | --------------------------------------------------- |
| **Type**               | `string`                                            |
| **Required**           | No                                                  |
| **Same definition as** | [keyIcon](#modules_items_anyOf_i1_oneOf_i1_keyIcon) |

**Description:** Set the icon to be displayed by `display.keyType: "icon"`

###### <a name="modules_items_anyOf_i1_oneOf_i70_keyWidth"></a>5.1.2.71.6. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > keyWidth`

|                        |                                                       |
| ---------------------- | ----------------------------------------------------- |
| **Type**               | `integer`                                             |
| **Required**           | No                                                    |
| **Default**            | `0`                                                   |
| **Same definition as** | [keyWidth](#modules_items_anyOf_i1_oneOf_i1_keyWidth) |

**Description:** Width of the module key. Use 0 to use `display.keyWidth`

###### <a name="modules_items_anyOf_i1_oneOf_i70_outputColor"></a>5.1.2.71.7. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > outputColor`

|                        |                                                             |
| ---------------------- | ----------------------------------------------------------- |
| **Type**               | `enum (of string)`                                          |
| **Required**           | No                                                          |
| **Same definition as** | [outputColor](#modules_items_anyOf_i1_oneOf_i1_outputColor) |

**Description:** Output color of the module. Left empty to use `display.color.output`

###### <a name="modules_items_anyOf_i1_oneOf_i70_format"></a>5.1.2.71.8. Property `JSON config > modules > modules items > anyOf > item 1 > oneOf > Zpool > format`

|                |                     |
| -------------- | ------------------- |
| **Type**       | `string`            |
| **Required**   | No                  |
| **Defined in** | #/$defs/zpoolFormat |

**Description:** Output format of the module `Zpool`. See Wiki for formatting syntax
    1. {name}: Zpool name
    2. {state}: Zpool state
    3. {used}: Size used
    4. {total}: Size total
    5. {used-percentage}: Size percentage num
    6. {fragmentation-percentage}: Fragmentation percentage num
    7. {used-percentage-bar}: Size percentage bar
    8. {fragmentation-percentage-bar}: Fragmentation percentage bar

##### <a name="modules_items_anyOf_i1_type"></a>5.1.2.72. Property `JSON config > modules > modules items > anyOf > item 1 > type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-05-15 at 14:22:12 +0200
