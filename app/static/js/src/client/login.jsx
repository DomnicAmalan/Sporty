import React from 'react'
import ReactDOM from 'react-dom'
import Axios from 'axios';
import { Redirect } from '../components/Redirect.jsx'

class Login extends React.Component{

    constructor(props){
        super(props);
        this.state = {}
    }


    async UNSAFE_componentWillMount(){
        this.setState({
            schema : [],
            urls: {},
            data: {},
            error_message: "",
            signed_in: false
        })
    }

    async componentDidMount(){
        Axios.get('/api/login/user/schema').then(res => {
            let data = {}
            res.data.schema.forEach(fields => {
                data[fields.name] = ""
            })
            this.setState({
                schema : res.data.schema,
                urls: res.data.urls,
                data: data
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
            res.data.status ? this.setState({signed_in: true}) : this.setState({error_message: res.data.message})
        })
    }

    render(){
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
            <div>Loggin You In</div>
        )

        return(
            <div>
                {this.state.error_message ? <strong>{this.state.error_message}</strong>:""}
                {this.state.signed_in ? <Redirect timeout={3000} redirect_url={'/'} message={redirect_message} /> : <div>{input}<button onClick={()=>this.handleSubmit()}>Log In</button></div>}
            </div>
        )
    }
}

ReactDOM.render(<Login/>, document.getElementById('login-main-container'));


