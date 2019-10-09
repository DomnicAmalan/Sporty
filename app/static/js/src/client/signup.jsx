import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';
import { FormCreator } from "../components/FormCreator.jsx";



class App extends React.Component {

    constructor(props){
        super(props);
        this.state = {

        }
        this.handleChange = this.handleChange.bind(this);
    }

    componentDidMount(){
        Axios.get("/api/schema/user/signup").then(res => {
            let data = res.data
            this.setState({
                schema: data.schema,
                urls: data.urls,
                data: {}
            })
        })
    }

    handleChange(e){
        let data = this.state.data
        data[e.target.name] = e.target.value
        this.setState({
            data: data
        })

    }

    render() {
        return (
           <FormCreator schema={this.state.schema} data = {this.state.data} handleChange={this.handleChange}/>
        );
    }
  }

  ReactDOM.render(<App/>, document.getElementById('signup-main-container'));
