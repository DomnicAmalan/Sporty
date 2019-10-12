import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';


class SignUp extends React.Component {
    

    constructor(props){
        super(props);

        this.state = {}
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    async UNSAFE_componentWillMount(){
        this.setState({
            schema : [],
            urls: {},
            data: {},
            errors: {}
        })
    }

    async componentDidMount(){
        Axios.get('/api/signup/user/schema').then(res => {
            let data = {}
            let errors = {}
            res.data.schema.forEach(fields => {
                data[fields.name] = ""
                errors[fields.name] = ""
            })
            this.setState({
                schema : res.data.schema,
                urls: res.data.urls,
                data: data,
                errors: errors
            })
        })
    }

    handleChange(e){
        let data = this.state.data
        const { name, value } = event.target;
        let errors = this.state.errors;

                
    }

    handleSubmit(){
        let urls = this.state.urls
        let data = this.state.data
        Axios.post(urls['submit_url'], data).then(res => {
            console.log(res.data)
        })
    }

    render() {
        let input = []
        this.state.schema.forEach(tag => {
            input.push(
                <div>
                    <label>{tag['field_name']}</label>
                    <input type="text" name={tag['name']} onChange={(e)=>this.handleChange(e)} required/>
                </div>
            )
        })
        return (
            <div>
                {input}
                <button onClick={()=>this.handleSubmit()}>Sign Up</button>
            </div>
        );
    }
  }

  ReactDOM.render(<SignUp/>, document.getElementById('signup-main-container'));
