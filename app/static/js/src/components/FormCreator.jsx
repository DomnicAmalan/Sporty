import React from 'react'
import ReactDOM from 'react-dom'


export class FormCreator extends React.Component {

    inputTag(){
        let schema = this.props.schema
        let data = this.props.data
        let value = []
        for (let tag in schema){
            value.push(<div><label>{schema[tag]["field_name"]}</label><input type={schema[tag]["type"]} value={data.tag} name={tag} onChange={e => this.props.handleChange(e)}></input></div>)
        }
        return value
    }

    render() {
        return (
           <div>{this.inputTag()}</div>
        );
    }
  }

