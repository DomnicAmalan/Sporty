import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';
import { Redirect } from '../components/Redirect.jsx'
import { DropdownExampleSearchDropdown } from '../components/Dropdown.jsx'



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
            countries: [],
            error_message: null,
            signed_up: false
        })
    }

    async componentDidMount(){
        Axios.get('/api/signup/user/schema').then(res => {
            let data = {}
            res.data.schema.forEach(fields => {
                data[fields.name] = ""
            })
            this.setState({
                schema : res.data.schema,
                urls: res.data.urls,
                data: data,
                countries: res.data.countries
            })
        })
    }

    handleChange(event){
        let data = this.state.data
        let { name, value } = event.target;
        data[name] = value;
        this.setState({
            data:data
        })
    }

    handleSubmit(){
        let urls = this.state.urls
        let data = this.state.data
        Axios.post(urls['submit_url'], data).then(res => {
            res.data.status ? this.setState({signed_up: true}) : this.setState({"error_message":res.data.message})
        })
    }

    render() {
        let input = []
        this.state.schema.forEach(tag => {
            input.push(
                <div>
                    <label>{tag['field_name']}</label>
                    <input type={tag["type"]} name={tag['name']} onChange={(e)=>this.handleChange(e)} required/>
                </div>
            )
        })

        let redirect_message=[]

        redirect_message.push(
            <div>
                Thank You For Registering
                <div>You will be redirected to Login. To go Now <a href="/login">Click Here</a></div>
            </div>
        )

        return (
            <div>
                {this.state.error_message ? <strong>{this.state.error_message}</strong>:""}
                {
                    this.state.signed_up ? <Redirect timeout={5000} redirect_url={'/login'} message={redirect_message}/> : 
                    <div>
                        {input}
                        <button onClick={()=>this.handleSubmit()}>Sign Up</button>
                    </div>
                }
            </div>
        );
    }
  }

  ReactDOM.render(<SignUp/>, document.getElementById('signup-main-container'));
