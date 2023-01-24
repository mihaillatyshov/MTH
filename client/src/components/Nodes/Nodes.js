import React, { useEffect, useState } from 'react'
import PrevNextNodes from './PrevNextNodes'
import NowNode from './NowNode'
import { ServerAPI_GET } from '../../libs/ServerAPI'
import { useParams } from 'react-router'

const Nodes = () => {
	const [nodes, setNodes] = useState(undefined)
	const params = useParams();
	const getPrevNext = (id) => {
		console.log(id ? id : 0)
		ServerAPI_GET({
			url : "/api/v1/graph/get_prev_next/" + (id ? id : 0),
			onDataReceived : (data) => setNodes(data.nodes)
		})
    }

    useEffect(() => {
        getPrevNext(params.id)
    }, [params.id])

	//const handleNodeChange = (id) => {
	//	getPrevNext(id)
	//}

	return (
		<div>
			{
				typeof nodes === 'undefined' ? (
					<div>Loading...</div>
				) : (
					<div className="row">
						<NowNode 	   node ={nodes.Now} />
						<PrevNextNodes nodesPrev={nodes.Prev} nodesNext={nodes.Next} />
					</div>
				)
			}
		</div>
	)
}

export default Nodes
