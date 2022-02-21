import AceEditor from "react-ace";
import React, { Component } from 'react';

import "ace-builds/src-noconflict/mode-sql";
import "ace-builds/src-noconflict/theme-vibrant_ink";

class CodeEditor extends Component {

  onChange(newValue: any) {
    // console.log("change", newValue);
  }

  render() {
    return (
      <AceEditor
        value="SELECT * FROM blocks LIMIT 10;"
        mode="sql"
        theme="vibrant_ink"
        onChange={this.onChange}
        name="codeEditor"
        editorProps={{ $blockScrolling: true }}
        setOptions={{
          enableBasicAutocompletion: true,
          enableLiveAutocompletion: true,
          enableSnippets: true
        }}
        width={"1000"}
        // height={"00"}
      />
    );
  }
}
export default CodeEditor